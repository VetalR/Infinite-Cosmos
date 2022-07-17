import os

import requests


def download_image(url, file_name):

    dir_images = os.path.abspath('images')

    response = requests.get(url)
    response.raise_for_status()

    with open(f'{dir_images}/{file_name}', 'wb') as file:
        file.write(response.content)
