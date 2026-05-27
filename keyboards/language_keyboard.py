from telebot import types

def get_language_keyboard():
    markup = types.InlineKeyboardMarkup()

    markup.add(
        types.InlineKeyboardButton("Українська 🇺🇦", callback_data="uk"),
        types.InlineKeyboardButton("English 🇬🇧", callback_data="en")
    )

    return markup