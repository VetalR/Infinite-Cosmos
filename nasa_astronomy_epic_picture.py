import os
from datetime import datetime
import requests
from dotenv import load_dotenv
import fnmatch


def get_nasa_astronomy_epic_picture(api_key):


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
            f'{img_date}/png/{img_name}.png'
        )
        response = requests.get(
            url=img_url,
            params=params
        )
        response.raise_for_status()

        file_name = f'nasa_epic_{files_count}.png'
        with open(f'{dir_image}/{file_name}', 'wb') as f:
            f.write(response.content)
        files_count += 1


if __name__ == '__main__':

    load_dotenv()
    api_key_nasa = os.getenv('API_KEY_NASA')

    now = datetime.now()
    get_nasa_astronomy_epic_picture(api_key_nasa)
    print(datetime.now()-now)
