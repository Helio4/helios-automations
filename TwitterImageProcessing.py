import tweepy
import os
import requests
import shutil
import json

def input_tweet(): # We assume the provided URL is valid
  url = input("Enter the Tweet's URL: ")
  return url.split('/')[-1].split('?')[0]

def make_tweet_shortcut(outputFolder, status):
  shortcut = open(outputFolder + "/Tweet.url", 'w')

  shortcut.write('[InternetShortcut]\n')
  shortcut.write('URL=https://twitter.com/{handle}/status/{id}'.format(handle=status.author.screen_name, id=status.id))
  
  shortcut.close()

def setup_folder(status):
  downloadFolder = config['download_root'] + "/@" + status.author.screen_name
  
  count = 1
  if not os.path.exists(downloadFolder):
    os.mkdir(downloadFolder)
  else:
    for path in os.listdir(downloadFolder):
      if not os.path.isfile(os.path.join(downloadFolder, path)):
          count += 1
  
  outputFolder = downloadFolder + "/" + str(count)
  os.mkdir(outputFolder)
  
  make_tweet_shortcut(outputFolder, status)
  
  return outputFolder

def reduce_noise(imgFolder, downloadFolder):
  waifuPath = config['waifu_path']
  os.chdir(waifuPath)
  print('Reducing noise...')
  os.system("waifu2x-caffe-cui.exe -i " + imgFolder + " -m noise -n 3 -o " + outputFolder)

def download_images(downloadFolderPath):
  os.mkdir(downloadFolderPath)
  number = 1
  
  print('Downloading Images...')
  for img in images:
    file = requests.get(img + "?name=orig")
    open(downloadFolderPath + '/original0{number}.png'.format(number=number), "wb").write(file.content)
    number = number + 1
  print('Downloaded!')

def open_config():
  global config
  
  configFile = open('./config.json')
  config = json.load(configFile)

  configFile.close()

def initiate_api():
  auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
  auth.set_access_token(config['access_token'], config['access_token_secret'])
  return tweepy.API(auth)

if __name__ == '__main__':
  open_config()

  api = initiate_api()

  tweetId = input_tweet()

  status = api.get_status(tweetId)
  
  images = list(map(lambda img: img['media_url'], status.extended_entities['media']))
  tempPath = dir_path = os.path.dirname(os.path.realpath(__file__)) + "/temp"

  download_images(tempPath)
  
  outputFolder = setup_folder(status)
  reduce_noise(tempPath, outputFolder)
  
  shutil.rmtree(tempPath)
  
  print('Completed!')
