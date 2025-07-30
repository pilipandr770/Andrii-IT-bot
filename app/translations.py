# translations.py

TRANSLATIONS = {
    'uk': {
        # Основні повідомлення
        'welcome_message': (
            "Привіт! Я бот з підтримкою голосових та текстових повідомлень.\n"
            "Надішли мені повідомлення, і я відповім тобі тією ж мовою.\n"
            "Щоб залишити свої контактні дані, скористайся кнопкою \"📝 Залишити контакт\" внизу екрану або командою /contact."
        ),
        'language_selected': "🇺🇦 Вибрано українську мову",
        'choose_language': "🌍 Оберіть мову / Choose language / Wählen Sie Sprache / Выберите язык:",
        
        # Кнопки меню
        'btn_start': "🚀 Старт",
        'btn_contact': "📝 Залишити контакт",
        'btn_language': "🌍 Мова",
        'btn_datenschutz': "🔒 Захист даних",
        'btn_agb': "📋 Умови користування",
        'btn_impressum': "ℹ️ Імпресум",
        
        # Контактна форма
        'contact_name': "Будь ласка, вкажіть ваше ім'я:",
        'contact_info': "Тепер залиште ваші контактні дані (телефон або email):",
        'contact_goal': "Яка мета вашого звернення? (Наприклад: Автоматизація, Консультація, Інше)",
        'contact_success': "Дякую, {name}! Ми зв'яжемося з вами за наданими даними.",
        'contact_cancelled': "Скасовано.",
        
        # Адмін
        'admin_new_request': "📥 <b>НОВА ЗАЯВКА</b>",
        'admin_no_permissions': "У вас немає прав для цієї дії.",
        'admin_no_requests': "Заявок ще немає.",
        'admin_requests_list': "Список заявок:",
        'admin_error_reading': "Сталася помилка при читанні заявок.",
        'admin_instructions_uploaded': "Інструкції успішно завантажені.",
        'admin_send_file': "Будь ласка, надішліть файл з інструкціями.",
        
        # Загальні
        'menu_select_action': "Оберіть дію з меню або напишіть повідомлення.",
        'bot_started': "Бот запущено...",
        
        # Нові сторінки
        'datenschutz_title': "🔒 ЗАХИСТ ПЕРСОНАЛЬНИХ ДАНИХ",
        'datenschutz_content': (
            "Ми серйозно ставимося до захисту ваших персональних даних.\n\n"
            "📋 Які дані ми збираємо:\n"
            "• Ім'я та контактні дані (при заповненні форми)\n"
            "• Повідомлення, які ви надсилаєте боту\n"
            "• Технічну інформацію (ID користувача Telegram)\n\n"
            "🎯 Для чого використовуємо:\n"
            "• Надання послуг через бот\n"
            "• Зв'язок з вами за вашим запитом\n"
            "• Покращення якості сервісу\n\n"
            "🔐 Безпека:\n"
            "• Дані зберігаються в захищеній базі\n"
            "• Не передаємо дані третім особам\n"
            "• Дотримуємося GDPR\n\n"
            "📧 Питання: pilipandr79@icloud.com"
        ),
        'agb_title': "📋 УМОВИ КОРИСТУВАННЯ",
        'agb_content': (
            "Умови користування ботом:\n\n"
            "✅ Дозволено:\n"
            "• Використання бота за призначенням\n"
            "• Надсилання коректних запитів\n"
            "• Залишення контактних даних для зв'язку\n\n"
            "❌ Заборонено:\n"
            "• Надсилання спам-повідомлень\n"
            "• Використання ненормативної лексики\n"
            "• Спроби зламати або пошкодити бот\n"
            "• Розповсюдження шкідливого контенту\n\n"
            "⚖️ Відповідальність:\n"
            "• Користувач несе відповідальність за свої дії\n"
            "• Ми залишаємо право заблокувати порушників\n"
            "• Сервіс надається \"як є\"\n\n"
            "📧 Питання: pilipandr79@icloud.com"
        ),
        'impressum_title': "ℹ️ ІМПРЕСУМ",
        'impressum_content': (
            "Neue Zeiten Bot\n\n"
            "�‍💼 Відповідальна особа:\n"
            "Pylypchuk Andrii\n\n"
            "📧 Email: pilipandr79@icloud.com\n"
            "📞 Телефон: +49 160 95030120\n\n"
            "⚖️ Відповідальність за контент:\n"
            "Pylypchuk Andrii\n"
            "Email: pilipandr79@icloud.com\n\n"
            "🤖 Про бота:\n"
            "Багатомовний Telegram-бот з інтеграцією OpenAI\n"
            "Підтримка: українська, російська, німецька, англійська"
        )
    },
    
    'ru': {
        # Основные сообщения
        'welcome_message': (
            "Привет! Я бот с поддержкой голосовых и текстовых сообщений.\n"
            "Отправь мне сообщение, и я отвечу тебе на том же языке.\n"
            "Чтобы оставить свои контактные данные, воспользуйся кнопкой \"📝 Оставить контакт\" внизу экрана или командой /contact."
        ),
        'language_selected': "🇷🇺 Выбран русский язык",
        'choose_language': "🌍 Выберите язык / Choose language / Wählen Sie Sprache / Оберіть мову:",
        
        # Кнопки меню
        'btn_start': "🚀 Старт",
        'btn_contact': "📝 Оставить контакт",
        'btn_language': "🌍 Язык",
        'btn_datenschutz': "🔒 Защита данных",
        'btn_agb': "📋 Условия использования",
        'btn_impressum': "ℹ️ Импрессум",
        
        # Контактная форма
        'contact_name': "Пожалуйста, укажите ваше имя:",
        'contact_info': "Теперь оставьте ваши контактные данные (телефон или email):",
        'contact_goal': "Какова цель вашего обращения? (Например: Автоматизация, Консультация, Другое)",
        'contact_success': "Спасибо, {name}! Мы свяжемся с вами по предоставленным данным.",
        'contact_cancelled': "Отменено.",
        
        # Админ
        'admin_new_request': "📥 <b>НОВАЯ ЗАЯВКА</b>",
        'admin_no_permissions': "У вас нет прав для этого действия.",
        'admin_no_requests': "Заявок еще нет.",
        'admin_requests_list': "Список заявок:",
        'admin_error_reading': "Произошла ошибка при чтении заявок.",
        'admin_instructions_uploaded': "Инструкции успешно загружены.",
        'admin_send_file': "Пожалуйста, пришлите файл с инструкциями.",
        
        # Общие
        'menu_select_action': "Выберите действие из меню или напишите сообщение.",
        'bot_started': "Бот запущен...",
        
        # Новые страницы
        'datenschutz_title': "🔒 ЗАЩИТА ПЕРСОНАЛЬНЫХ ДАННЫХ",
        'datenschutz_content': (
            "Мы серьезно относимся к защите ваших персональных данных.\n\n"
            "📋 Какие данные мы собираем:\n"
            "• Имя и контактные данные (при заполнении формы)\n"
            "• Сообщения, которые вы отправляете боту\n"
            "• Техническую информацию (ID пользователя Telegram)\n\n"
            "🎯 Для чего используем:\n"
            "• Предоставление услуг через бот\n"
            "• Связь с вами по вашему запросу\n"
            "• Улучшение качества сервиса\n\n"
            "🔐 Безопасность:\n"
            "• Данные хранятся в защищенной базе\n"
            "• Не передаем данные третьим лицам\n"
            "• Соблюдаем GDPR\n\n"
            "📧 Вопросы: pilipandr79@icloud.com"
        ),
        'agb_title': "📋 УСЛОВИЯ ИСПОЛЬЗОВАНИЯ",
        'agb_content': (
            "Условия использования бота:\n\n"
            "✅ Разрешено:\n"
            "• Использование бота по назначению\n"
            "• Отправка корректных запросов\n"
            "• Оставление контактных данных для связи\n\n"
            "❌ Запрещено:\n"
            "• Отправка спам-сообщений\n"
            "• Использование ненормативной лексики\n"
            "• Попытки взломать или повредить бот\n"
            "• Распространение вредоносного контента\n\n"
            "⚖️ Ответственность:\n"
            "• Пользователь несет ответственность за свои действия\n"
            "• Мы оставляем право заблокировать нарушителей\n"
            "• Сервис предоставляется \"как есть\"\n\n"
            "📧 Вопросы: pilipandr79@icloud.com"
        ),
        'impressum_title': "ℹ️ ИМПРЕССУМ",
        'impressum_content': (
            "Neue Zeiten Bot\n\n"
            "�‍💼 Ответственное лицо:\n"
            "Pylypchuk Andrii\n\n"
            "📧 Email: pilipandr79@icloud.com\n"
            "📞 Телефон: +49 160 95030120\n\n"
            "⚖️ Ответственность за контент:\n"
            "Pylypchuk Andrii\n"
            "Email: pilipandr79@icloud.com\n\n"
            "🤖 О боте:\n"
            "Многоязычный Telegram-бот с интеграцией OpenAI\n"
            "Поддержка: украинский, русский, немецкий, английский"
        )
    },
    
    'de': {
        # Grundlegende Nachrichten
        'welcome_message': (
            "Hallo! Ich bin ein Bot mit Unterstützung für Sprach- und Textnachrichten.\n"
            "Sende mir eine Nachricht und ich antworte dir in derselben Sprache.\n"
            "Um deine Kontaktdaten zu hinterlassen, nutze die Schaltfläche \"📝 Kontakt hinterlassen\" unten oder den Befehl /contact."
        ),
        'language_selected': "🇩🇪 Deutsche Sprache gewählt",
        'choose_language': "🌍 Sprache wählen / Choose language / Выберите язык / Оберіть мову:",
        
        # Menü-Schaltflächen
        'btn_start': "🚀 Start",
        'btn_contact': "📝 Kontakt hinterlassen",
        'btn_language': "🌍 Sprache",
        'btn_datenschutz': "🔒 Datenschutz",
        'btn_agb': "📋 AGB",
        'btn_impressum': "ℹ️ Impressum",
        
        # Kontaktformular
        'contact_name': "Bitte geben Sie Ihren Namen an:",
        'contact_info': "Hinterlassen Sie nun Ihre Kontaktdaten (Telefon oder E-Mail):",
        'contact_goal': "Was ist das Ziel Ihrer Anfrage? (Z.B.: Automatisierung, Beratung, Anderes)",
        'contact_success': "Danke, {name}! Wir werden uns über die angegebenen Daten bei Ihnen melden.",
        'contact_cancelled': "Abgebrochen.",
        
        # Admin
        'admin_new_request': "📥 <b>NEUE ANFRAGE</b>",
        'admin_no_permissions': "Sie haben keine Berechtigung für diese Aktion.",
        'admin_no_requests': "Es gibt noch keine Anfragen.",
        'admin_requests_list': "Liste der Anfragen:",
        'admin_error_reading': "Fehler beim Lesen der Anfragen.",
        'admin_instructions_uploaded': "Anweisungen erfolgreich hochgeladen.",
        'admin_send_file': "Bitte senden Sie eine Datei mit Anweisungen.",
        
        # Allgemein
        'menu_select_action': "Wählen Sie eine Aktion aus dem Menü oder schreiben Sie eine Nachricht.",
        'bot_started': "Bot gestartet...",
        
        # Neue Seiten
        'datenschutz_title': "🔒 DATENSCHUTZ",
        'datenschutz_content': (
            "Wir nehmen den Schutz Ihrer persönlichen Daten ernst.\n\n"
            "📋 Welche Daten wir sammeln:\n"
            "• Name und Kontaktdaten (beim Ausfüllen des Formulars)\n"
            "• Nachrichten, die Sie an den Bot senden\n"
            "• Technische Informationen (Telegram Benutzer-ID)\n\n"
            "🎯 Wofür wir sie verwenden:\n"
            "• Bereitstellung von Dienstleistungen über den Bot\n"
            "• Kontaktaufnahme auf Ihre Anfrage\n"
            "• Verbesserung der Servicequalität\n\n"
            "🔐 Sicherheit:\n"
            "• Daten werden in einer sicheren Datenbank gespeichert\n"
            "• Keine Weitergabe an Dritte\n"
            "• DSGVO-konform\n\n"
            "📧 Fragen: pilipandr79@icloud.com"
        ),
        'agb_title': "📋 ALLGEMEINE GESCHÄFTSBEDINGUNGEN",
        'agb_content': (
            "Nutzungsbedingungen für den Bot:\n\n"
            "✅ Erlaubt:\n"
            "• Bestimmungsgemäße Nutzung des Bots\n"
            "• Senden korrekter Anfragen\n"
            "• Hinterlassen von Kontaktdaten für die Kommunikation\n\n"
            "❌ Verboten:\n"
            "• Versenden von Spam-Nachrichten\n"
            "• Verwendung von Schimpfwörtern\n"
            "• Versuche, den Bot zu hacken oder zu beschädigen\n"
            "• Verbreitung schädlicher Inhalte\n\n"
            "⚖️ Verantwortung:\n"
            "• Der Benutzer ist für seine Handlungen verantwortlich\n"
            "• Wir behalten uns das Recht vor, Störer zu blockieren\n"
            "• Service wird \"wie besehen\" bereitgestellt\n\n"
            "📧 Fragen: pilipandr79@icloud.com"
        ),
        'impressum_title': "ℹ️ IMPRESSUM",
        'impressum_content': (
            "Neue Zeiten Bot\n\n"
            "�‍💼 Verantwortliche Person:\n"
            "Pylypchuk Andrii\n\n"
            "📧 E-Mail: pilipandr79@icloud.com\n"
            "📞 Telefon: +49 160 95030120\n\n"
            "⚖️ Verantwortlich für den Inhalt:\n"
            "Pylypchuk Andrii\n"
            "E-Mail: pilipandr79@icloud.com\n\n"
            "🤖 Über den Bot:\n"
            "Mehrsprachiger Telegram-Bot mit OpenAI-Integration\n"
            "Unterstützte Sprachen: Ukrainisch, Russisch, Deutsch, Englisch"
        )
    },
    
    'en': {
        # Basic messages
        'welcome_message': (
            "Hello! I'm a bot with support for voice and text messages.\n"
            "Send me a message and I'll respond in the same language.\n"
            "To leave your contact details, use the \"📝 Leave contact\" button at the bottom or the /contact command."
        ),
        'language_selected': "🇺🇸 English language selected",
        'choose_language': "🌍 Choose language / Wählen Sie Sprache / Выберите язык / Оберіть мову:",
        
        # Menu buttons
        'btn_start': "🚀 Start",
        'btn_contact': "📝 Leave contact",
        'btn_language': "🌍 Language",
        'btn_datenschutz': "🔒 Privacy Policy",
        'btn_agb': "📋 Terms of Service",
        'btn_impressum': "ℹ️ Imprint",
        
        # Contact form
        'contact_name': "Please enter your name:",
        'contact_info': "Now leave your contact details (phone or email):",
        'contact_goal': "What is the purpose of your inquiry? (E.g.: Automation, Consultation, Other)",
        'contact_success': "Thank you, {name}! We will contact you using the provided details.",
        'contact_cancelled': "Cancelled.",
        
        # Admin
        'admin_new_request': "📥 <b>NEW REQUEST</b>",
        'admin_no_permissions': "You don't have permission for this action.",
        'admin_no_requests': "No requests yet.",
        'admin_requests_list': "List of requests:",
        'admin_error_reading': "Error reading requests.",
        'admin_instructions_uploaded': "Instructions uploaded successfully.",
        'admin_send_file': "Please send a file with instructions.",
        
        # General
        'menu_select_action': "Select an action from the menu or write a message.",
        'bot_started': "Bot started...",
        
        # New pages
        'datenschutz_title': "🔒 PRIVACY POLICY",
        'datenschutz_content': (
            "We take the protection of your personal data seriously.\n\n"
            "📋 What data we collect:\n"
            "• Name and contact details (when filling out the form)\n"
            "• Messages you send to the bot\n"
            "• Technical information (Telegram user ID)\n\n"
            "🎯 What we use it for:\n"
            "• Providing services through the bot\n"
            "• Contacting you upon your request\n"
            "• Improving service quality\n\n"
            "🔐 Security:\n"
            "• Data is stored in a secure database\n"
            "• No sharing with third parties\n"
            "• GDPR compliant\n\n"
            "📧 Questions: pilipandr79@icloud.com"
        ),
        'agb_title': "📋 TERMS OF SERVICE",
        'agb_content': (
            "Terms of use for the bot:\n\n"
            "✅ Allowed:\n"
            "• Using the bot as intended\n"
            "• Sending appropriate requests\n"
            "• Leaving contact details for communication\n\n"
            "❌ Prohibited:\n"
            "• Sending spam messages\n"
            "• Using inappropriate language\n"
            "• Attempting to hack or damage the bot\n"
            "• Distributing harmful content\n\n"
            "⚖️ Responsibility:\n"
            "• User is responsible for their actions\n"
            "• We reserve the right to block violators\n"
            "• Service provided \"as is\"\n\n"
            "📧 Questions: pilipandr79@icloud.com"
        ),
        'impressum_title': "ℹ️ IMPRINT",
        'impressum_content': (
            "Neue Zeiten Bot\n\n"
            "�‍💼 Responsible person:\n"
            "Pylypchuk Andrii\n\n"
            "📧 Email: pilipandr79@icloud.com\n"
            "📞 Phone: +49 160 95030120\n\n"
            "⚖️ Responsible for content:\n"
            "Pylypchuk Andrii\n"
            "Email: pilipandr79@icloud.com\n\n"
            "🤖 About the bot:\n"
            "Multilingual Telegram bot with OpenAI integration\n"
            "Supported languages: Ukrainian, Russian, German, English"
        )
    }
}

def get_text(lang_code, key, **kwargs):
    """Получить переведенный текст по ключу и языку"""
    if lang_code not in TRANSLATIONS:
        lang_code = 'en'  # Язык по умолчанию
    
    text = TRANSLATIONS[lang_code].get(key, TRANSLATIONS['en'].get(key, key))
    
    # Форматирование если есть параметры
    if kwargs:
        try:
            return text.format(**kwargs)
        except KeyError:
            return text
    
    return text

def get_language_buttons():
    """Получить кнопки выбора языка"""
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
    
    keyboard = [
        [
            InlineKeyboardButton("🇺🇦 Українська", callback_data="lang_uk"),
            InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")
        ],
        [
            InlineKeyboardButton("🇩🇪 Deutsch", callback_data="lang_de"),
            InlineKeyboardButton("🇺🇸 English", callback_data="lang_en")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
