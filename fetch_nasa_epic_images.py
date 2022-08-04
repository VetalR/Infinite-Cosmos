import fnmatch
import os

import requests
from dotenv import load_dotenv

from image_loader import download_image


def main():
    load_dotenv()
    nasa_api_key = os.getenv('API_KEY_NASA')

    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': nasa_api_key
    }
    response = requests.get(
        url=epic_url,
        params=params
    )
    response.raise_for_status()

    epic_suite = response.json()

    images = os.path.abspath('images')
    files_count = len(fnmatch.filter(os.listdir(images), 'nasa_epic_*'))

    for image in epic_suite:

        img_name = image['image']
        img_date = image['date'].split()[0].replace('-', '/')
        img_url = (
            f'https://api.nasa.gov/EPIC/archive/natural/'
            f'{img_date}/png/{img_name}.png?api_key={nasa_api_key}'
        )

        file_name = f'nasa_epic_{files_count}.png'
        download_image(img_url, file_name)
        files_count += 1


if __name__ == '__main__':
    main()
