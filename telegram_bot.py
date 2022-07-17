import os

import telegram
from dotenv import load_dotenv


def main(token):
    bot = telegram.Bot(token=token)
    updates = bot.get_updates()
    bot.send_message(text='Kkkk', chat_id=733023967)


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')

    main(telegram_token)
