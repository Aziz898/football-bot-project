import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_FOOTBALL_URL = "https://v3.football.api-sports.io/fixtures"
API_KEY = os.getenv("FOOTBALL_API_KEY")

HEADERS = {
    "x-apisports-key": API_KEY
}

def get_today_matches():
    from datetime import datetime
    today = datetime.now().strftime("%Y-%m-%d")

    params = {
        "date": today,
        "timezone": "Europe/Moscow"  # Поменяй на свой часовой пояс, если нужно
    }

    try:
        response = requests.get(API_FOOTBALL_URL, headers=HEADERS, params=params)
        response.raise_for_status()
        matches = response.json()['response']
        return matches
    except Exception as e:
        print(f"Ошибка при получении матчей: {e}")
        return []
