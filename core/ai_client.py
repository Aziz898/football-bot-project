import os
from openai import OpenAI

# Твой GitHub Token и endpoint
GITHUB_TOKEN = "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"
ENDPOINT_URL = "https://models.inference.ai.azure.com"
MODEL_NAME = "gpt-4o"

# Инициализация клиента
client = OpenAI(
    base_url=ENDPOINT_URL,
    api_key=GITHUB_TOKEN,
)

# Функция генерации текста
def generate_text(prompt, temperature=0.7, max_tokens=500):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Ты — футбольный журналист. Пиши яркие, живые новости о футболе.",
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=temperature,
            top_p=1.0,
            max_tokens=max_tokens,
            model=MODEL_NAME
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Ошибка генерации текста через AI: {e}")
        return None
