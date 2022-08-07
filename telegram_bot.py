import os
import random
import time
import argparse
import telegram
from dotenv import load_dotenv

PUBLICATION_TIME = 14400


def send_picture():
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.getenv('CHAT_ID')

    bot = telegram.Bot(token=telegram_token)
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
            with open(f'images/{img}', 'rb') as file:
                bot.send_document(
                    chat_id=telegram_chat_id,
                    document=file.read()
                )

            if args.seconds_delay:
                time.sleep(args.seconds_delay)
            else:
                time.sleep(PUBLICATION_TIME)


if __name__ == '__main__':
    send_picture()
