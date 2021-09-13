# Helio's Automations
This is a list of small scripts I have made to make my life easier and avoid a lot of repetitive tasks. These are intended for my own personal use, so they are not exactly "user-friendly," but free to ask if you need help using them or installing dependencies!
## List of scripts and what they do:
* [DLsiteMetadataDownloader.py](https://github.com/Helio4/helios-automations/blob/main/DLsiteMetadataDownloader.py): Given a DLsite RJ code, this script will scrap the metadata for the product page and apply it to the mp3 files. This is intended for music or voice dramas.
* [TwitterImageProcessing.py](https://github.com/Helio4/helios-automations/blob/main/TwitterImageProcessing.py): Given a Tweet URL it will download its images, denoise them using  [waifu2x-caffe](https://github.com/lltcggie/waifu2x-caffe) and sort them into the right folder, adding a shortcut file to the tweet in said folder. The config.json file is formated as follows: <details>
  <summary>Configuration file</summary>
  
  ```json
  {
    "consumer_key": "TWITTER_CONSUMER_KEY_GOES_HERE",
    "consumer_secret": "TWITTER_CONSUMER_SECRET_GOES_HERE",
    "access_token": "TWITTER_ACCESS_TOKEN_GOES_HERE",
    "access_token_secret": "TWITTER_ACCESS_TOKEN_SECRET_GOES_HERE",
    "download_root": "ABSOLUTE_PATH_TO_WHERE_YOU_WANNA_SORT_YOUR_IMAGES",
    "waifu_path": "ABSOLUTE_PATH_TO_WAIFU2X-CAFFE_FOLDER"
  }
  ```
</details>
