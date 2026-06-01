from services.providers.provider_router import generate_with_provider
from services.prompt_loader import load_prompt


def generate_response(user_message, mode, lang, history):

    system_prompt = load_prompt(mode, lang)

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    messages.extend(history)

    messages.append({
        "role": "user",
        "content": user_message
    })

    return generate_with_provider(messages)