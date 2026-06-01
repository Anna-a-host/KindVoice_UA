from groq import Groq

from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_groq(messages):

    completion = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=messages,

        temperature=0.7,

        max_tokens=200
    )

    return (
        completion
        .choices[0]
        .message
        .content
    )