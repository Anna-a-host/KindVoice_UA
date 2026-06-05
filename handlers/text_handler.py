from data.user_profiles import user_profiles
from services.ai_service import generate_response

from time import sleep
from database.user_repository import *


def setup_text_handler(bot):

    @bot.message_handler(func=lambda message: True)
    def handle_text(message):

        chat_id = message.chat.id

        if chat_id not in user_profiles:
            profile = get_user_profile(chat_id)
            if profile and profile.get("lang"):
                user_profiles[chat_id] = {
                    "lang": profile["lang"],
                    "mode": profile.get("mode", "general"),
                    "history": []
                }
            else:
                bot.send_message(chat_id, "Please use /start to set your language and mode first! 🤗")
                return

        profile = user_profiles[chat_id]
        lang = profile["lang"]
        mode = profile.get("mode", "general")


        sleep(0.7)
        bot.send_chat_action(chat_id, "typing")
        sleep(0.5)
        
        history = profile.get("history", [])

        try:
            history.append({
                "role": "user",
                "content": message.text
            })

            history = history[-8:]

            response = generate_response(
                lang=lang,
                mode=mode,
                history=history
            )

            bot.send_message(chat_id, response)
            increase_message_count(chat_id)

            history.append({
                "role": "assistant",
                "content": response
            })

            history = history[-8:]

            profile["history"] = history

        except Exception as e:

            print(e)

            fallback = (
                "Я поруч 💙"
                if lang == "uk"
                else "I am here 💙"
            )

            bot.send_message(chat_id, fallback)