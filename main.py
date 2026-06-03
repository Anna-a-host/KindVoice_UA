import telebot

from config import TELEGRAM_TOKEN

from keyboards.language_keyboard import get_language_keyboard

from handlers.text_handler import setup_text_handler
from handlers.callback_handler import setup_callback_handler
from handlers.voice_handler import setup_voice_handler
from time import sleep
from database.user_repository import add_user
from database.statistics import *
from database.init_db import create_tables

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'reset'])
def start(message):

    chat_id = message.chat.id
    add_user(message.chat.id)
    sleep(0.7)
    bot.send_chat_action(chat_id, "typing")
    sleep(0.5)

    bot.send_chat_action(chat_id, "typing")
    bot.send_message(
        message.chat.id,
        "Вітаю! 😊 Оберіть мову для спілкування / \nHello there! 😊 Choose language for communication:",
        reply_markup=get_language_keyboard()
    )


@bot.message_handler(commands=['stats'])
def stats(message):
    
    print_dashboard()
    print_all_users()

    bot.send_message(
        message.chat.id,
        "Statistics printed in console."
    )


setup_text_handler(bot)
setup_callback_handler(bot)
setup_voice_handler(bot)

create_tables()
print("Bot is running...")
bot.infinity_polling()