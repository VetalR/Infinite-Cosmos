import argparse
import fnmatch
import os

import requests


def main():

    spacex = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(spacex)
    response.raise_for_status()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--start_number',
        help='You can choose Spacex launch number',
        type=int
    )
    args = parser.parse_args()

    list_start = response.json()

    start_number = None

    if not args.start_number:
        list_start.reverse()
        for start in list_start:
            if start["links"]["flickr_images"]:
                start_number = start["links"]["flickr_images"]
                break
    else:
        for start in list_start:
            if start['flight_number'] == args.start_number:
                if start["links"]["flickr_images"]:
                    start_number = start["links"]["flickr_images"]
                    break
                if not start["links"]["flickr_images"]:
                    print('No images')
                    break
            if args.start_number > len(list_start):
                print('Spacex has less starts, than you input')
                break

    if start_number:
        dir_image = os.path.abspath('images')
        files_count = len(fnmatch.filter(os.listdir(dir_image), 'spacex_*'))
        for url in start_number:

            response = requests.get(url)
            response.raise_for_status()

            file_name = f'spacex_{files_count}.jpg'
            with open(f'{dir_image}/{file_name}', 'wb') as file:
                file.write(response.content)

            files_count += 1


if __name__ == '__main__':
    main()
