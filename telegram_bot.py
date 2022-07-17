import os

import telegram
from dotenv import load_dotenv


def send_message(token, chat_id):
    bot = telegram.Bot(token=token)
    bot.send_message(text='Hello', chat_id=chat_id)


def send_picture(token, chat_id):
    bot = telegram.Bot(token=token)
    bot.send_document(chat_id=chat_id, document=open('images/spacex_1.jpg', 'rb'))


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.getenv('CHAT_ID')

    # send_message(telegram_token, telegram_chat_id)
    send_picture(telegram_token, telegram_chat_id)