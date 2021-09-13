# Helio's Automations
This is a list of small scripts I have made to make my life easier and avoid a lot of repetitive tasks. These are intended for my own personal use, so they are not exactly "user-friendly," but feel free to ask me if you need help using them or installing dependencies!
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

* [set-styles-by-actor.lua](https://github.com/Helio4/helios-automations/blob/main/Aegisub%20Scripts/set-styles-by-actor.lua): This Aegisub script changes the style of every line based on their actor. If there's a style that exactly matches the actor then the style will be changed to that one. Very useful if, like me, you like doing the translation in a plain text file first.
* [hide-original-text.lua](https://github.com/Helio4/helios-automations/blob/main/Aegisub%20Scripts/hide-original-text.lua): This Aegisub script will put between brackets the contents of a line. I use this for the official [Holo no Graffiti](https://www.youtube.com/watch?v=vF2-vhOkYLs&list=PL1NeGg1woXqngQytLzL8lJJLYwmzk1Wuq) Spanish subs, that way the Japanese text is conserved but hidden at the same time, making proofreading for my translation partner easier.
