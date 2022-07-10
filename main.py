import requests


def download_image(url, path):

    file_name = 'dvmn_example'

    response = requests.get(url)
    response.raise_for_status()

    with open(f'{path}{file_name}', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':

    urls = 'https://dvmn.org/media/HST-SM4.jpeg'
    img_path = 'images/'
    download_image(urls, img_path)
