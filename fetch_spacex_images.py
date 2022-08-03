import argparse
import fnmatch
import os

import requests

from main import download_image


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

    spacex_starts = response.json()

    start_number = None

    if not args.start_number:
        spacex_starts.reverse()
        for start in spacex_starts:
            if start["links"]["flickr_images"]:
                start_number = start["links"]["flickr_images"]
                break
    else:
        for start in spacex_starts:
            if start['flight_number'] == args.start_number:
                if start["links"]["flickr_images"]:
                    start_number = start["links"]["flickr_images"]
                    break
                if not start["links"]["flickr_images"]:
                    print('No images')
                    break
            if args.start_number > len(spacex_starts):
                print('Spacex has less starts, than you input')
                break

    if start_number:
        dir_image = os.path.abspath('images')
        files_count = len(fnmatch.filter(os.listdir(dir_image), 'spacex_*'))

        for url in start_number:
            file_name = f'spacex_{files_count}.jpg'
            download_image(url, file_name)
            files_count += 1


if __name__ == '__main__':
    main()
