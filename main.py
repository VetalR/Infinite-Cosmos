import requests
from pprint import pprint


def download_image(url, path):

    file_name = 'dvmn_example'

    response = requests.get(url)
    response.raise_for_status()

    with open(f'{path}{file_name}', 'wb') as f:
        f.write(response.content)


def get_space_x_start_image():

    url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(url)
    response.raise_for_status()

    for start in response.json():
        if start["links"]["flickr_images"]:
            pprint(start["links"]["flickr_images"], sort_dicts=False)


if __name__ == '__main__':

    get_space_x_start_image()

    # urls = 'https://dvmn.org/media/HST-SM4.jpeg'
    # img_path = 'images/'
    # download_image(urls, img_path)
