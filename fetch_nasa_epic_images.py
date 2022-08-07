import fnmatch
import os

import requests
from dotenv import load_dotenv

from image_loader import download_image


def main():
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')

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
        img_date, _ = image['date'].replace('-', '/').split()

        img_url = (
            f'https://api.nasa.gov/EPIC/archive/natural/'
            f'{img_date}/png/{img_name}.png'
        )

        file_name = f'nasa_epic_{files_count}.png'
        download_image(
            url=img_url,
            file_name=file_name,
            params=params
        )
        files_count += 1


if __name__ == '__main__':
    main()
