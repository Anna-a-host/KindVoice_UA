from telebot import types

def get_state_keyboard(lang):
    markup = types.InlineKeyboardMarkup()

    temp = {
        "uk": {
            "panic": "Паніка 🆘",
            "war": "Війна 🛡️",
            "anxiety": "Тривога 😰",
            "calm": "Спокій ✨",
            "support": "Підтримка 💙",
            "integration": "ВПО 🤝",
            "general": "Розмова 💬"
        },
        "en": {
            "panic": "Panic 🆘",
            "war": "War 🛡️",
            "anxiety": "Anxiety 😰",
            "calm": "Calm ✨",
            "support": "Support 💙",
            "integration": "IDP 🤝",
            "general": "General 💬"
        }
    }

    temp = temp[lang]

    markup.row(
        types.InlineKeyboardButton(temp["panic"], callback_data="panic"),
        types.InlineKeyboardButton(temp["war"], callback_data="war")
    )

    markup.row(
        types.InlineKeyboardButton(temp["anxiety"], callback_data="anxiety"),
        types.InlineKeyboardButton(temp["calm"], callback_data="calm")
    )

    markup.row(
        types.InlineKeyboardButton(temp["support"], callback_data="support"),
        types.InlineKeyboardButton(temp["integration"], callback_data="integration")
    )

    markup.add(
        types.InlineKeyboardButton(temp["general"], callback_data="general")
    )

    return markup