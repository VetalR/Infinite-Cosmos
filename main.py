from urllib.parse import urlparse
import os
import requests
import fnmatch


def download_image(url, file_name):

    dir_image = os.path.abspath('images')

    response = requests.get(url)
    response.raise_for_status()

    with open(f'{dir_image}/{file_name}', 'wb') as file:
        file.write(response.content)



    # dir_image = os.path.abspath('images')
    #
    #
    # files_count = len(fnmatch.filter(os.listdir(dir_image), 'spacex_*'))
    #
    # for url in urls:
    #     response = requests.get(url)
    #     response.raise_for_status()
    #     # file_format = get_file_format(url=url)
    #
    #     file_name = f'spacex_{files_count}{file_format}'
    #     with open(f'{dir_image}/{file_name}', 'wb') as f:
    #         f.write(response.content)
    #
    #     files_count += 1
    #
    #
    #
    # dir_image = os.path.abspath('images')
    # files_count = len(fnmatch.filter(os.listdir(dir_image), 'spacex_*'))
    # for url in start_number:
    #
    #     response = requests.get(url)
    #     response.raise_for_status()
    #
    #     file_name = f'spacex_{files_count}.jpg'
    #     with open(f'{dir_image}/{file_name}', 'wb') as file:
    #         file.write(response.content)
    #
    #         files_count += 1

if __name__ == '__main__':
    url = 'https://live.staticflickr.com/65535/50630802488_8cc373728e_o.jpg'
    download_image(url)


