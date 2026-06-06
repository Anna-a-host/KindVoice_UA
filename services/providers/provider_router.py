from services.providers.gemini_provider import generate_gemini
from services.providers.openrouter_provider import generate_openrouter
from services.providers.groq_provider import generate_groq


def generate_with_provider(messages):

    try:
        print("Trying Groq...")
        return generate_groq(messages)

    except Exception as e:
        print("Groq failed:", e)


    try:
        print("Trying Gemini...")
        return generate_gemini(messages)

    except Exception as e:

        print("Gemini failed:", e)
        
    
    try:
        print("Trying OpenRouter...")
        return generate_openrouter(messages)

    except Exception as e:
        print("OpenRouter failed:", e)

        raise Exception(
            "All providers failed."
        )