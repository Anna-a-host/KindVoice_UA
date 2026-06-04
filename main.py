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

import os
from flask import Flask, request

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive and running!"

@app.route(f'/{TELEGRAM_TOKEN}', methods=['POST'])
def receive_update():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.stream.read().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return 'Invalid request', 403


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
    print_total_users()
    print_popular_modes()
    print_top_users()

    bot.send_message(
        message.chat.id,
        "Statistics printed in console."
    )

setup_text_handler(bot)
setup_callback_handler(bot)
setup_voice_handler(bot)

create_tables()

if __name__ == "__main__":
    bot.remove_webhook()
    RENDER_URL = os.environ.get("RENDER_EXTERNAL_URL")
    
    webhook_url = f"{RENDER_URL}/{TELEGRAM_TOKEN}"
    bot.set_webhook(url=webhook_url)
    print(f"Webhook successfully set to: {webhook_url}")
    
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
