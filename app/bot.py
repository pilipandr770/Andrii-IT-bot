import os
import logging
import sqlite3
from datetime import datetime
from telegram import Update, Bot, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, ContextTypes, CommandHandler,
    MessageHandler, ConversationHandler, filters, CallbackQueryHandler
)
from openai_client import generate_text_via_assistant, generate_text_via_assistant_with_thread, generate_image, generate_image_prompt_via_assistant
from dotenv import load_dotenv
from translations import get_text, get_language_buttons

# Load environment
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID", "0"))  # optional, for /set_instructions

# States for contact conversation
STATE_NAME, STATE_CONTACT, STATE_GOAL = range(3)

# In-memory storage for system instructions and user languages
system_instructions = None
user_languages = {}  # Хранение языка пользователя {user_id: lang_code}

# Configure logging
logging.basicConfig(
    format='[%(asctime)s] %(levelname)s: %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

DB_FILE = os.path.join(os.path.dirname(__file__), "contacts.db")

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        name TEXT,
        contact TEXT,
        goal TEXT,
        user_id INTEGER
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS user_languages (
        user_id INTEGER PRIMARY KEY,
        language_code TEXT DEFAULT 'en'
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS user_threads (
        user_id INTEGER PRIMARY KEY,
        thread_id TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

def get_user_language(user_id):
    """Получить язык пользователя из базы данных"""
    global user_languages
    if user_id in user_languages:
        return user_languages[user_id]
    
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT language_code FROM user_languages WHERE user_id = ?", (user_id,))
    result = c.fetchone()
    conn.close()
    
    if result:
        lang = result[0]
        user_languages[user_id] = lang
        return lang
    else:
        # Если пользователь новый, показываем выбор языка
        return None

def set_user_language(user_id, language_code):
    """Сохранить язык пользователя в базе данных"""
    global user_languages
    user_languages[user_id] = language_code
    
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO user_languages (user_id, language_code) VALUES (?, ?)", 
              (user_id, language_code))
    conn.commit()
    conn.close()

def get_user_thread_id(user_id):
    """Получает thread_id для пользователя или создает новый"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT thread_id FROM user_threads WHERE user_id = ?", (user_id,))
    result = c.fetchone()
    
    if result:
        thread_id = result[0]
        is_new_thread = False
    else:
        # Создаем новый thread для пользователя
        import openai
        thread = openai.beta.threads.create()
        thread_id = thread.id
        c.execute("INSERT INTO user_threads (user_id, thread_id) VALUES (?, ?)", 
                  (user_id, thread_id))
        conn.commit()
        is_new_thread = True
    
    conn.close()
    return thread_id, is_new_thread

def is_thread_empty(thread_id):
    """Проверяет, пустой ли thread (нет сообщений)"""
    import openai
    try:
        messages = openai.beta.threads.messages.list(thread_id=thread_id, limit=1)
        return len(messages.data) == 0
    except:
        return True

def reset_user_thread(user_id):
    """Сбрасывает thread пользователя (создает новый)"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # Создаем новый thread
    import openai
    thread = openai.beta.threads.create()
    thread_id = thread.id
    
    c.execute("INSERT OR REPLACE INTO user_threads (user_id, thread_id) VALUES (?, ?)", 
              (user_id, thread_id))
    conn.commit()
    conn.close()
    return thread_id

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id)
    
    # Если язык не установлен, показываем выбор языка
    if user_lang is None:
        await update.message.reply_text(
            get_text('en', 'choose_language'),
            reply_markup=get_language_buttons()
        )
        return
    
    # Если язык установлен, показываем главное меню
    await show_main_menu(update, context, user_lang)

async def reset_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Сбросить контекст разговора пользователя"""
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id) or 'en'
    
    # Создаем новый thread для пользователя
    reset_user_thread(user_id)
    
    await update.message.reply_text(get_text(user_lang, 'conversation_reset'))
    await show_main_menu(update, context, user_lang)

async def show_main_menu(update, context, user_lang):
    """Показать главное меню с кнопками на выбранном языке"""
    keyboard = [
        [KeyboardButton(get_text(user_lang, 'btn_start'))],
        [KeyboardButton(get_text(user_lang, 'btn_contact'))],
        [
            KeyboardButton(get_text(user_lang, 'btn_language')),
            KeyboardButton(get_text(user_lang, 'btn_datenschutz'))
        ],
        [
            KeyboardButton(get_text(user_lang, 'btn_agb')),
            KeyboardButton(get_text(user_lang, 'btn_impressum'))
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False, is_persistent=True)
    
    # Определяем тип события (message или callback_query)
    if hasattr(update, 'callback_query') and update.callback_query:
        await update.callback_query.message.reply_text(
            get_text(user_lang, 'welcome_message'),
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            get_text(user_lang, 'welcome_message'),
            reply_markup=reply_markup
        )

async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка выбора языка"""
    query = update.callback_query
    await query.answer()
    
    user_id = update.effective_user.id
    language_code = query.data.split('_')[1]  # lang_uk -> uk
    
    set_user_language(user_id, language_code)
    
    await query.edit_message_text(get_text(language_code, 'language_selected'))
    await show_main_menu(update, context, language_code)

async def show_language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать выбор языка"""
    await update.message.reply_text(
        get_text('en', 'choose_language'),
        reply_markup=get_language_buttons()
    )

async def show_datenschutz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать страницу защиты данных"""
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id) or 'en'
    
    title = get_text(user_lang, 'datenschutz_title')
    content = get_text(user_lang, 'datenschutz_content')
    
    await update.message.reply_text(f"{title}\n\n{content}")

async def show_agb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать страницу условий использования"""
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id) or 'en'
    
    title = get_text(user_lang, 'agb_title')
    content = get_text(user_lang, 'agb_content')
    
    await update.message.reply_text(f"{title}\n\n{content}")

async def show_impressum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать страницу импрессум"""
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id) or 'en'
    
    title = get_text(user_lang, 'impressum_title')
    content = get_text(user_lang, 'impressum_content')
    
    await update.message.reply_text(f"{title}\n\n{content}")

async def set_instructions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Only admin can upload instructions
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id) or 'en'
    
    if user_id != ADMIN_USER_ID:
        return await update.message.reply_text(get_text(user_lang, 'admin_no_permissions'))
    if update.message.document:
        file = await update.message.document.get_file()
        path = await file.download_to_drive(custom_path="instructions.txt")
        global system_instructions
        with open(path, encoding='utf-8') as f:
            system_instructions = f.read()
        await update.message.reply_text(get_text(user_lang, 'admin_instructions_uploaded'))
    else:
        await update.message.reply_text(get_text(user_lang, 'admin_send_file'))

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id) or 'en'
    
    # Получаем thread_id для пользователя
    thread_id, is_new_thread = get_user_thread_id(user_id)
    
    # Проверяем, пустой ли thread
    is_first_message = is_new_thread or is_thread_empty(thread_id)
    
    # Формируем системную инструкцию с учетом языка
    global system_instructions
    language_names = {
        'uk': 'украинской',
        'ru': 'русском', 
        'de': 'немецком',
        'en': 'английском'
    }
    lang_instruction = f"Отвечай на {language_names.get(user_lang, 'английском')} языке."
    
    # Объединяем системные инструкции
    combined_system_instruction = None
    if is_first_message:
        if system_instructions:
            combined_system_instruction = f"{system_instructions}\n\n{lang_instruction}"
        else:
            combined_system_instruction = lang_instruction
    
    # Используем контекстную функцию
    reply = generate_text_via_assistant_with_thread(
        thread_id=thread_id,
        user_message=user_text,
        system_instruction=combined_system_instruction,
        is_first_message=is_first_message
    )
    
    await update.message.reply_text(reply)

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice = update.message.voice
    file = await voice.get_file()
    path = await file.download_to_drive(custom_path="voice.ogg")
    # Транскрибируем через OpenAI Whisper (новый API)
    import openai
    audio_file = open(path, "rb")
    transcript_obj = openai.audio.transcriptions.create(model="whisper-1", file=audio_file)
    transcript = transcript_obj.text
    
    # Генерируем ответ с учетом языка пользователя и контекста
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id) or 'en'
    
    # Получаем thread_id для пользователя
    thread_id, is_new_thread = get_user_thread_id(user_id)
    
    # Проверяем, пустой ли thread
    is_first_message = is_new_thread or is_thread_empty(thread_id)
    
    # Формируем системную инструкцию с учетом языка
    global system_instructions
    language_names = {
        'uk': 'украинской',
        'ru': 'русском', 
        'de': 'немецком',
        'en': 'английском'
    }
    lang_instruction = f"Отвечай на {language_names.get(user_lang, 'английском')} языке."
    
    # Объединяем системные инструкции
    combined_system_instruction = None
    if is_first_message:
        if system_instructions:
            combined_system_instruction = f"{system_instructions}\n\n{lang_instruction}"
        else:
            combined_system_instruction = lang_instruction
    
    # Используем контекстную функцию
    reply = generate_text_via_assistant_with_thread(
        thread_id=thread_id,
        user_message=transcript,
        system_instruction=combined_system_instruction,
        is_first_message=is_first_message
    )
    
    await update.message.reply_text(reply)

async def contact_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id) or 'en'
    await update.message.reply_text(get_text(user_lang, 'contact_name'))
    return STATE_NAME

async def contact_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id) or 'en'
    
    # Проверяем, не нажал ли пользователь кнопку меню
    text = update.message.text
    menu_buttons = [
        get_text(user_lang, 'btn_start'),
        get_text(user_lang, 'btn_language'),
        get_text(user_lang, 'btn_datenschutz'),
        get_text(user_lang, 'btn_agb'),
        get_text(user_lang, 'btn_impressum')
    ]
    
    if text in menu_buttons:
        # Завершаем conversation и обрабатываем кнопку меню
        await handle_menu_buttons(update, context)
        return ConversationHandler.END
    
    context.user_data['contact_name'] = update.message.text
    await update.message.reply_text(get_text(user_lang, 'contact_info'))
    return STATE_CONTACT

async def contact_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id) or 'en'
    
    # Проверяем, не нажал ли пользователь кнопку меню
    text = update.message.text
    menu_buttons = [
        get_text(user_lang, 'btn_start'),
        get_text(user_lang, 'btn_language'),
        get_text(user_lang, 'btn_datenschutz'),
        get_text(user_lang, 'btn_agb'),
        get_text(user_lang, 'btn_impressum')
    ]
    
    if text in menu_buttons:
        # Завершаем conversation и обрабатываем кнопку меню
        await handle_menu_buttons(update, context)
        return ConversationHandler.END
    
    context.user_data['contact_info'] = update.message.text
    await update.message.reply_text(get_text(user_lang, 'contact_goal'))
    return STATE_GOAL

async def contact_goal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id) or 'en'
    
    # Проверяем, не нажал ли пользователь кнопку меню
    text = update.message.text
    menu_buttons = [
        get_text(user_lang, 'btn_start'),
        get_text(user_lang, 'btn_language'),
        get_text(user_lang, 'btn_datenschutz'),
        get_text(user_lang, 'btn_agb'),
        get_text(user_lang, 'btn_impressum')
    ]
    
    if text in menu_buttons:
        # Завершаем conversation и обрабатываем кнопку меню
        await handle_menu_buttons(update, context)
        return ConversationHandler.END
    
    name = context.user_data.get('contact_name')
    info = context.user_data.get('contact_info')
    goal = update.message.text
    timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
    
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("INSERT INTO contacts (date, name, contact, goal, user_id) VALUES (?, ?, ?, ?, ?)",
                  (timestamp, name, info, goal, user_id))
        conn.commit()
        conn.close()
        logger.info(f"[DEBUG] Заявка успешно записана в базу: {DB_FILE}")
    except Exception as e:
        logger.error(f"Ошибка записи в базу контактов: {e}")
    
    # Отправляем уведомление админу
    admin_id = ADMIN_USER_ID
    admin_msg = (
        f"{get_text('ru', 'admin_new_request')}\n"
        f"<b>Имя:</b> {name}\n"
        f"<b>Контакт:</b> {info}\n"
        f"<b>Цель:</b> {goal}\n"
        f"<b>User ID:</b> {user_id}\n"
        f"<b>Время:</b> {timestamp}"
    )
    await context.bot.send_message(
        chat_id=admin_id,
        text=admin_msg,
        parse_mode='HTML'
    )
    
    logger.info(f"Contact data received: {name} - {info} - {goal} - {user_id}")
    await update.message.reply_text(get_text(user_lang, 'contact_success', name=name))
    return ConversationHandler.END

async def cancel_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id) or 'en'
    await update.message.reply_text(get_text(user_lang, 'contact_cancelled'))
    return ConversationHandler.END

async def leads_report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id) or 'en'
    
    if user_id != ADMIN_USER_ID:
        return await update.message.reply_text(get_text(user_lang, 'admin_no_permissions'))
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT date, name, contact, goal, user_id FROM contacts ORDER BY id DESC")
        rows = c.fetchall()
        conn.close()
        if not rows:
            await update.message.reply_text(get_text(user_lang, 'admin_no_requests'))
            return
        text = get_text(user_lang, 'admin_requests_list') + "\n"
        for row in rows:
            text += f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}\n"
        await update.message.reply_text(text)
    except Exception as e:
        logger.error(f"Ошибка чтения базы контактов: {e}")
        await update.message.reply_text(get_text(user_lang, 'admin_error_reading'))

async def handle_menu_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id) or 'en'
    
    # Проверяем кнопки только для текущего языка пользователя
    if text == get_text(user_lang, 'btn_start'):
        return await start(update, context)
    elif text == get_text(user_lang, 'btn_language'):
        return await show_language_selection(update, context)
    elif text == get_text(user_lang, 'btn_datenschutz'):
        return await show_datenschutz(update, context)
    elif text == get_text(user_lang, 'btn_agb'):
        return await show_agb(update, context)
    elif text == get_text(user_lang, 'btn_impressum'):
        return await show_impressum(update, context)
    else:
        # Если кнопка не распознана, попробуем проверить другие языки
        # Это для случаев, когда пользователь еще не выбрал язык или изменил язык
        for lang in ['uk', 'ru', 'de', 'en']:
            if lang == user_lang:
                continue  # Уже проверили выше
            
            if text == get_text(lang, 'btn_start'):
                return await start(update, context)
            elif text == get_text(lang, 'btn_language'):
                return await show_language_selection(update, context)
            elif text == get_text(lang, 'btn_datenschutz'):
                return await show_datenschutz(update, context)
            elif text == get_text(lang, 'btn_agb'):
                return await show_agb(update, context)
            elif text == get_text(lang, 'btn_impressum'):
                return await show_impressum(update, context)
        
        # Если ничего не найдено, показываем сообщение по умолчанию
        await update.message.reply_text(get_text(user_lang, 'menu_select_action'))

if __name__ == '__main__':
    init_db()
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    # Callback query handlers для выбора языка
    app.add_handler(CallbackQueryHandler(language_callback, pattern=r"^lang_"))
    
    # Basic handlers
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('reset', reset_conversation))
    app.add_handler(CommandHandler('set_instructions', set_instructions))
    app.add_handler(CommandHandler('leads', leads_report))
    
    # Conversation for contact с поддержкой всех языков
    contact_patterns = []
    for lang in ['uk', 'ru', 'de', 'en']:
        contact_patterns.append(f"^{get_text(lang, 'btn_contact')}$")
    
    conv = ConversationHandler(
        entry_points=[
            CommandHandler('contact', contact_start),
            MessageHandler(filters.TEXT & ~filters.COMMAND & filters.Regex("|".join(contact_patterns)), contact_start)
        ],
        states={
            STATE_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, contact_name)],
            STATE_CONTACT: [MessageHandler(filters.TEXT & ~filters.COMMAND, contact_info)],
            STATE_GOAL: [MessageHandler(filters.TEXT & ~filters.COMMAND, contact_goal)],
        },
        fallbacks=[CommandHandler('cancel', cancel_contact)]
    )
    app.add_handler(conv)
    
    # Menu button handlers для всех кнопок меню (кроме контакта, который обрабатывается в ConversationHandler)
    # Создаем паттерны для всех языков, но обработка будет приоритетно по языку пользователя
    menu_patterns = []
    for lang in ['uk', 'ru', 'de', 'en']:
        menu_patterns.extend([
            f"^{get_text(lang, 'btn_start')}$",
            f"^{get_text(lang, 'btn_language')}$",
            f"^{get_text(lang, 'btn_datenschutz')}$",
            f"^{get_text(lang, 'btn_agb')}$",
            f"^{get_text(lang, 'btn_impressum')}$"
        ])
    
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND & filters.Regex("|".join(menu_patterns)), 
        handle_menu_buttons
    ))
    
    # Text and voice handlers (должны быть последними)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    
    logger.info(get_text('ru', 'bot_started'))
    app.run_polling()
