import requests

from config import OPENROUTER_API_KEY


def generate_openrouter(messages):

    response = requests.post(

        "https://openrouter.ai/api/v1/chat/completions",

        headers={
            "Authorization":
            f"Bearer {OPENROUTER_API_KEY}"
        },

        json={
            "model":
            "deepseek/deepseek-chat-v3-0324",

            "messages":
            messages
        }
    )

    return response.json()["choices"][0]["message"]["content"]