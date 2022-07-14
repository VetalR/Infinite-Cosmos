from urllib.parse import urlparse
import os
from datetime import datetime
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


def fetch_spacex_last_launch():

    spacex = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(spacex)
    response.raise_for_status()

    list_start = response.json()
    list_start.reverse()

    last_start = None
    for start in list_start:
        if start["links"]["flickr_images"]:
            last_start = start["links"]["flickr_images"]
            break

    dir_image = os.path.abspath('images')
    files_count = len(fnmatch.filter(os.listdir(dir_image), 'spacex_*'))
    for url in last_start:

        response = requests.get(url)
        response.raise_for_status()

        file_format = get_file_format(url=url)
        file_name = f'spacex_{files_count}{file_format}'
        with open(f'{dir_image}/{file_name}', 'wb') as f:
            f.write(response.content)

        files_count += 1



def get_file_format(url):
    url_path = urlparse(url).path
    return os.path.splitext(url_path)[1]


def get_nasa_astronomy_picture_of_the_day(api_key):

    url = 'https://api.nasa.gov/planetary/apod'
    # url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': api_key,
        'hd': True,
        'count': 10
    }

    response = requests.get(
        url=url,
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

    # now = datetime.now()
    # get_nasa_astronomy_picture_of_the_day(api_key_nasa)
    # print(datetime.now()-now)

    fetch_spacex_last_launch()
