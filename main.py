from urllib.parse import urlparse
import os
from datetime import datetime
import requests


def download_image(urls):

    dir_image = os.path.abspath('images')
    files_count = len(os.listdir(dir_image))

    for url in urls:
        response = requests.get(url)
        response.raise_for_status()

        file_name = f'spacex_{files_count}.jpg'
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

    img_list = get_spacex_start_image()[-1]
    download_image(img_list)


if __name__ == '__main__':

    fetch_spacex_last_launch()
