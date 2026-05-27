from groq import Groq

from config import GROQ_API_KEY

from services.model_router import choose_model
from services.prompt_loader import load_prompt


client = Groq(api_key=GROQ_API_KEY)


def generate_response(history, mode, lang):

    model_name = choose_model(mode)

    system_prompt = load_prompt(mode, lang)

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    messages.extend(history)


    completion = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.4,
        max_tokens=140
    )

    return (
        completion
        .choices[0]
        .message
        .content
    )