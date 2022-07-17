import fnmatch
import os

import requests
from dotenv import load_dotenv

from main import download_image


def main(api_key):

    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': api_key
    }
    response = requests.get(
        url=epic_url,
        params=params
    )

    epic_list = response.json()

    dir_image = os.path.abspath('images')
    files_count = len(fnmatch.filter(os.listdir(dir_image), 'nasa_epic_*'))
    params = {
        'api_key': api_key
    }

    for image in epic_list:

        img_name = image['image']
        img_date = image['date'].split()[0].replace('-', '/')
        img_url = (
            f'https://api.nasa.gov/EPIC/archive/natural/'
            f'{img_date}/png/{img_name}.png?api_key={api_key}'
        )

        file_name = f'nasa_epic_{files_count}.png'
        download_image(img_url, file_name)
        files_count += 1


if __name__ == '__main__':

    load_dotenv()
    api_key_nasa = os.getenv('API_KEY_NASA')
    main(api_key_nasa)
