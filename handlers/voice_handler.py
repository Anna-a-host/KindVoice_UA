import os

from services.voice_service import transcribe_audio
from services.ai_service import generate_response

from data.user_profiles import user_profiles
from time import sleep


def setup_voice_handler(bot):

    @bot.message_handler(content_types=['voice'])
    def handle_voice(message):

        chat_id = message.chat.id
        bot.send_chat_action(chat_id, "typing")

        if chat_id not in user_profiles:

            bot.send_message(
                chat_id,
                "Please select language first with /start"
            )
            return

        sleep(0.7)
        bot.send_chat_action(chat_id, "typing")
        sleep(0.5)

        try:
            file_info = bot.get_file(message.voice.file_id)
            downloaded_file = bot.download_file(
                file_info.file_path
            )

            voice_path = f"temp_{chat_id}.ogg"

            with open(voice_path, "wb") as file:
                file.write(downloaded_file)

            text = transcribe_audio(voice_path)
            profile = user_profiles[chat_id]

            lang = profile.get("lang", "en")
            mode = profile.get("mode", "general")
            history = profile.get("history", [])

            history.append({
                "role": "user",
                "content": text
            })

            history = history[-8:]

            response = generate_response(
                text,
                history=history,
                lang=lang,
                mode=mode
            )

            bot.send_message(chat_id, response)

            history.append({
                "role": "assistant",
                "content": response
            })

            history = history[-8:]

            profile["history"] = history
            os.remove(voice_path)

        except Exception as e:

            import traceback

            error = traceback.format_exc()

            print(error)

            bot.send_message(
                chat_id,
                f"Voice error:\n\n{error[:4000]}"
            )