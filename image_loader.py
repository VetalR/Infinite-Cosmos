from pathlib import Path

import requests


def download_image(url, file_name, params=None):

    dir_images = Path('images').resolve().joinpath(file_name)

    response = requests.get(
        url=url,
        params=params
    )
    response.raise_for_status()

    Path(dir_images).write_bytes(response.content)
