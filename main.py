from urllib.parse import urlparse
import os
from datetime import datetime
from pprint import pprint
import requests
from dotenv import load_dotenv
import fnmatch


def download_image(urls):

    dir_image = os.path.abspath('images')
    files_count = len(fnmatch.filter(os.listdir(dir_image), 'spacex_*'))

    for url in urls:
        response = requests.get(url)
        response.raise_for_status()
        file_format = get_file_format(url=url)

        file_name = f'spacex_{files_count}{file_format}'
        with open(f'{dir_image}/{file_name}', 'wb') as f:
            f.write(response.content)

        files_count += 1


def get_spacex_start_image():

    url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(url)
    response.raise_for_status()

    list_start = []
    for start in response.json():
        if start["links"]["flickr_images"]:
            list_start.append(start["links"]["flickr_images"])

    return list_start


def get_nasa_astronomy_epic_picture(api_key):

    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'

    params = {
        'api_key': api_key
    }
    response = requests.get(
        url=epic_url,
        params=params
    )

    epic_list = response.json()[:10]
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
    # get_nasa_astronomy_picture_of_the_day(api_key_nasa)
    get_nasa_astronomy_epic_picture(api_key_nasa)
    print(datetime.now()-now)

    # fetch_spacex_last_launch()
