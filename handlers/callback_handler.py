from data.user_profiles import user_profiles
from keyboards.state_keyboard import get_state_keyboard

def setup_callback_handler(bot):

    @bot.callback_query_handler(func=lambda call: call.data in ["uk", "en"])
    def handle_language(call):

        chat_id = call.message.chat.id
        lang = call.data

        if chat_id not in user_profiles:
            user_profiles[chat_id] = {}

        user_profiles[chat_id] = {
            "lang": lang,
            "history": []
        }

        text = (
            "Tell me how you are feeling 🤗"
            if lang == "en"
            else "Оберіть, як ви себе почуваєте 🤗"
        )

        bot.edit_message_text(
            text,
            chat_id,
            call.message.message_id,
            reply_markup=get_state_keyboard(lang)
        )

        bot.answer_callback_query(call.id)



    @bot.callback_query_handler(
        func=lambda call: call.data in [
            "panic", "war", "anxiety",
            "calm", "support",
            "integration", "general"
        ]
    )
    def handle_mode(call):

        chat_id = call.message.chat.id
        mode = call.data

        if chat_id not in user_profiles:
            user_profiles[chat_id] = {
                "lang": "en"
            }

        user_profiles[chat_id]["mode"] = mode

        lang = user_profiles[chat_id]["lang"]

        confirm_text = (
            "I’m here 💙 Tell me what’s going on."
            if lang == "en"
            else "Я поруч 💙 Напиши, що тебе турбує."
        )

        bot.edit_message_text(
            confirm_text,
            chat_id,
            call.message.message_id
        )

        bot.answer_callback_query(call.id)