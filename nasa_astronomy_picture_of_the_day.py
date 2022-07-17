from urllib.parse import urlparse
import os
from datetime import datetime
from pprint import pprint
import requests
from dotenv import load_dotenv
import fnmatch
import argparse


def get_file_format(url):
    url_path = urlparse(url).path
    return os.path.splitext(url_path)[1]


def main(api_key):

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--img_count',
        help='You can choose, how many photos do you need',
        type=int
    )
    args = parser.parse_args()

    img_count = 10
    if args.img_count:
        img_count = args.img_count

    apod_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'hd': True,
        'count': img_count
    }

    response = requests.get(
        url=apod_url,
        params=params
    )

    dir_image = os.path.abspath('images')
    files_count = len(fnmatch.filter(os.listdir(dir_image), 'nasa_apod_*'))

    for image in response.json():
        file_format = get_file_format(url=image['url'])
        if file_format:
            response = requests.get(image['url'])
            response.raise_for_status()
            file_name = f'nasa_apod_{files_count}{file_format}'
            with open(f'{dir_image}/{file_name}', 'wb') as f:
                f.write(response.content)
            files_count += 1


if __name__ == '__main__':
    load_dotenv()
    api_key_nasa = os.getenv('API_KEY_NASA')

    main(api_key_nasa)
