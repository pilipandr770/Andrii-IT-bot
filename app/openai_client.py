# openai_client.py

import os
import openai
import time
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_TEXT_ASSISTANT_ID = os.getenv("OPENAI_TEXT_ASSISTANT_ID").strip()
openai.api_key = OPENAI_API_KEY

def generate_text_via_assistant(prompt_msgs):
    # prompt_msgs — список dict з ролями та контентом
    # Використання OpenAI Assistants API (threads + messages)
    thread = openai.beta.threads.create()
    # Додаємо всі повідомлення користувача та системи
    for msg in prompt_msgs:
        if msg["role"] == "user":
            openai.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=msg["content"]
            )
        elif msg["role"] == "system":
            openai.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=f"[SYSTEM]: {msg['content']}"
            )
    run = openai.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=OPENAI_TEXT_ASSISTANT_ID
    )
    # Чекаємо завершення run (polling)
    while True:
        run_status = openai.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.status == "completed":
            break
        time.sleep(1)
    messages = openai.beta.threads.messages.list(thread_id=thread.id)
    # Відповідь асистента — останнє повідомлення з role='assistant'
    for msg in reversed(messages.data):
        if msg.role == "assistant":
            return msg.content[0].text.value
    return "Вибачте, не вдалося отримати відповідь від асистента."

def generate_text_via_assistant_with_thread(thread_id, user_message, system_instruction=None, is_first_message=False):
    """Генерирует ответ используя существующий thread для сохранения контекста"""
    
    # Добавляем системную инструкцию только если это первое сообщение в thread
    if system_instruction and is_first_message:
        openai.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=f"[SYSTEM]: {system_instruction}"
        )
    
    # Добавляем сообщение пользователя
    openai.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_message
    )
    
    # Запускаем ассистента
    run = openai.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=OPENAI_TEXT_ASSISTANT_ID
    )
    
    # Ждем завершения
    while True:
        run_status = openai.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
        if run_status.status == "completed":
            break
        elif run_status.status == "failed":
            return "Извините, произошла ошибка при обработке вашего сообщения."
        time.sleep(1)
    
    # Получаем последнее сообщение ассистента
    messages = openai.beta.threads.messages.list(thread_id=thread_id)
    for msg in messages.data:
        if msg.role == "assistant":
            return msg.content[0].text.value
    
    return "Извините, не удалось получить ответ от ассистента."


def generate_image_prompt_via_assistant(prompt_msgs):
    # Отримати промпт для картинки через текстового асистента
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=prompt_msgs,
        # Якщо треба — можна додати assistant_id=OPENAI_IMAGE_ASSISTANT_ID
    )
    return response.choices[0].message.content


def generate_image(prompt):
    # TODO: Реалізуйте генерацію зображення через OpenAI або асистента
    return "Генерація зображення ще не реалізована."
