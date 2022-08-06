import argparse
import fnmatch
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

from image_loader import download_image


def main():
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--img_count',
        help='You can choose, how many photos do you need',
        type=int,
        default=10
    )
    args = parser.parse_args()

    apod_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': nasa_api_key,
        'hd': True,
        'count': args.img_count
    }

    response = requests.get(
        url=apod_url,
        params=params
    )
    response.raise_for_status()

    dir_image = os.path.abspath('images')
    files_count = len(fnmatch.filter(os.listdir(dir_image), 'nasa_apod_*'))

    for image in response.json():
        file_format = os.path.splitext(urlparse(url=image['url']).path)[1]
        if file_format:
            file_name = f'nasa_apod_{files_count}{file_format}'
            download_image(image['url'], file_name)
            files_count += 1


if __name__ == '__main__':
    main()
