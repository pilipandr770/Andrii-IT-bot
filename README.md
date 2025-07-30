# Neue Zeiten - Telegram Bot с ИИ

Многофункциональный Telegram бот с поддержкой OpenAI для обработки текстовых и голосовых сообщений.

## Функциональность

- Обработка текстовых сообщений через OpenAI Assistant
- Транскрибирование и обработка голосовых сообщений
- Сбор контактной информации через форму контактов
- Административные функции для управления ботом

## Технологии

- Python 3.10+
- python-telegram-bot
- OpenAI API (GPT, Whisper)
- SQLite для хранения данных
- Docker для развертывания

## Настройка

### Переменные окружения

Создайте файл `.env` в директории `/app` со следующими переменными:

```
# Telegram Bot
TELEGRAM_TOKEN=your_telegram_token
ADMIN_USER_ID=your_admin_user_id

# OpenAI API
OPENAI_API_KEY=your_openai_api_key
OPENAI_TEXT_ASSISTANT_ID=your_assistant_id
```

## Запуск

### Локально

```bash
cd app
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
pip install -r requirements.txt
python bot.py
```

### Docker

```bash
cd app
docker build -t telegram_bot .
docker run -d --name telegram_bot_container telegram_bot
```

## Деплой на Render

Проект настроен для автоматического развертывания на платформе Render как фоновый воркер.
