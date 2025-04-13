from telegram import Bot
from telegram.ext import ApplicationBuilder, CommandHandler
import logging
import os
from core.db import SessionLocal, Match, Post, Log

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Твои реальные данные
TELEGRAM_TOKEN = '8081045765:AAHLb3diLQH7zj_5RS785i0VZoP2lvX049c'
CHANNEL_ID = '-1002501563624'  # ID канала

# Инициализация бота
bot = Bot(token=TELEGRAM_TOKEN)

# Создание приложения
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# Простая команда проверки работы
async def start(update, context):
    await update.message.reply_text('Бот работает!')

app.add_handler(CommandHandler('start', start))

# Функция для отправки сообщений в канал
async def send_channel_message(text):
    try:
        await bot.send_message(chat_id=CHANNEL_ID, text=text)
    except Exception as e:
        logging.error(f"Ошибка отправки сообщения: {e}")
        save_log('ERROR', f"Ошибка отправки сообщения: {e}")

# Функция для записи лога в базу
def save_log(level, message):
    db = SessionLocal()
    log = Log(level=level, message=message)
    db.add(log)
    db.commit()
    db.close()

if __name__ == '__main__':
    print("Запуск Telegram-бота...")
    app.run_polling()
