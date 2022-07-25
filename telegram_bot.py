import os
import random
import time
import argparse
import telegram
from dotenv import load_dotenv

PUBLICATION_TIME = 14400


def send_picture(token, chat_id):
    bot = telegram.Bot(token=token)
    img_list = os.listdir('images/')
    random.shuffle(img_list)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--seconds_delay',
        help='You can set the posting time in seconds',
        type=int
    )
    args = parser.parse_args()

    while True:
        for img in img_list:
            bot.send_document(
                chat_id=chat_id,
                document=open(f'images/{img}', 'rb')
            )

            if args.seconds_delay:
                time.sleep(args.seconds_delay)
            else:
                time.sleep(PUBLICATION_TIME)


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.getenv('CHAT_ID')

    send_picture(telegram_token, telegram_chat_id)
