# Space Telegram

# Project description
* This project provide posting images to Telegram bot
* Download images from Nasa and SpaceX

# Project Goals
* The code is written for educational purposes on online-course for web-developers https://dvmn.org

## How to install
* To install it, make sure you have Python 3.8 or greater installed
* Copy application from repo: 
  ```
  git clone https://github.com/VetalR/Infinite-Cosmos.git
  ```

## Get token and API key
* Generate token key NASA, from link https://api.nasa.gov
* Generate token key Telegram bot
* Create file into project directory `.env`
  * Set into `.env` file a variable `API_KEY_NASA` and use value `generated NASA token key`
  * Set into `.env` file a variable `TELEGRAM_BOT_TOKEN`and use value `generated Telegram token key`
    * Variable NASA example: `API_KEY_NASA=17c09e20ad155405123ac1977542fecf00231da7`
    * Variable Telegram example: `TELEGRAM_BOT_TOKEN=1234556789:AAA-GFuBvlJGiiTFN4dZWbtJnDM5-WvpSvc`

## How to use
* Activate your virtual environment
* Create or get current chat id of telegram bot 
  * Set into `.env` file a variable `CHAT_ID`
* Run script to install the required packages 
  ```
  pip3 install -r {path/}Infinite-Cosmos/requirements.txt
  ```
* Use Telegram posting
  * Run script, without argument 
    ```
    python {path/}Infinite-Cosmos/telegram_bot.py
    ```
    * One image will be post every 4 hours
  * Run script, without argument 
    ```
    python {path/}Infinite-Cosmos/telegram_bot.py --seconds_delay {posting time delay}
    ```
* Download SpaceX images
  * Run script, without argument 
    ```
    python {path/}Infinite-Cosmos/fetch_spacex_images.py
    ```
    * Download last SpaceX start images
  * Run script, without argument 
    ```
    python {path/}Infinite-Cosmos/fetch_spacex_images.py --start_number {start number}
    ```
    * Load images of selected starts SpaceX
* Download NASA APOD images
  * Run script, without argument 
    ```
    python {path/}Infinite-Cosmos/fetch_nasa_apod_images.py
    ```
    * Download 10 APOD images
  * Run script, without argument 
    ```
    python {path/}Infinite-Cosmos/fetch_nasa_apod_images.py --img_count {images count}
    ```
    * Download given APOD images count
* Download NASA EPIC images
  * Run script, without argument 
    ```
    python {path/}Infinite-Cosmos/fetch_nasa_epic_images.py
    ```
    * Download All EPIC images of day

## Simple Example
* To execute it: 
  ```
  python3 telegram_bot.py
  ```
* Example output: Images pubished to Telegram