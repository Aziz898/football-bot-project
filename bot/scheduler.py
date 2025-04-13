from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot.bot import send_channel_message
import asyncio

# Планировщик
scheduler = AsyncIOScheduler()

# Задачи

from core.football_api import get_today_matches

async def morning_matches():
    matches = get_today_matches()
    if matches:
        text = "⚽ Матчи на сегодня:\n\n"
        for match in matches:
            home = match['teams']['home']['name']
            away = match['teams']['away']['name']
            time = match['fixture']['date'][11:16]  # Часы:Минуты
            text += f"{time} - {home} vs {away}\n"
    else:
        text = "Сегодня нет запланированных матчей."

    await send_channel_message(text)
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
