from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot.bot import send_channel_message
import asyncio

# Планировщик
scheduler = AsyncIOScheduler()

# Задачи

async def morning_matches():
    # Здесь будет код получения матчей на сегодня (пока тестовый текст)
    await send_channel_message("Доброе утро! Вот список матчей на сегодня... (пока тестовый текст)")

async def afternoon_news():
    # Здесь будет код генерации новостей через нейросеть (пока тестовый текст)
    await send_channel_message("Дневная новость или факт о футболе! (пока тестовый текст)")

async def evening_news():
    # Здесь будет код для вечернего поста (пока тестовый текст)
    await send_channel_message("Вечерний факт о футболе! (пока тестовый текст)")

# Функция запуска планировщика
def start_scheduler():
    scheduler.add_job(morning_matches, 'cron', hour=8, minute=0)
    scheduler.add_job(afternoon_news, 'cron', hour=13, minute=0)
    scheduler.add_job(evening_news, 'cron', hour=18, minute=0)
    scheduler.start()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    start_scheduler()
    loop.run_forever()
