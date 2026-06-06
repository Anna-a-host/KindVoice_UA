import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def transcribe_audio(audio_path):
    with open(audio_path, "rb") as file: 
        translation = client.audio.transcriptions.create(
            file=("voice.ogg", file.read()), 
            model="whisper-large-v3", 
            response_format="text"
        )
    return translation
