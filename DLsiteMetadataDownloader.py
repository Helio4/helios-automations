from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error, TAL, TP1
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import os
import json

def input_code():  # input product code
    code = input('Enter the product code: ')
    url = 'https://www.dlsite.com/maniax/work/=/product_id/{code}.html'.format(
        code=code)
    response = requests.get(url)
    if response.status_code == 200:
        return code
    elif response.status_code == 404:
        print('Invalid product code, try again!')
        code = input_code()
        return code
    else:
        print('Something happened, try again!')
        code = input_code()
        return code

def input_audio_path():  # input audio file path (.mp3)
    path = input('Enter the Path to a directory or audio file: ')
    if os.path.isfile(path) and path.endswith('mp3'):
        return [path]
    elif os.path.isdir(path):
        file_paths = []
        for(dirname, dirs, files) in os.walk(path):
            for filename in files:
                if filename.endswith('mp3'):
                    file_paths.append(os.path.join(dirname, filename))
            break  # Prevents loop from exploring subdirectories
        return file_paths
    else:
        print('Wrong path entered, try again!')  # warning message
        file_paths = input_audio_path()
        return file_paths

def retrive_cover_art(code):
    chobit_url = requests.get(
        'https://chobit.cc/api/v1/dlsite/embed?workno={code}'.format(code=code))
    chobit_response = chobit_url.content.decode('utf-8')[9:-1]
    response_object = json.loads(chobit_response)
    if response_object['count'] == 0:
        code_num = int(code[2:])
        code_prefix = code[:2]
        leftover = code_num % 1000
        if leftover > 0:
            code_num = code_num - leftover + 1000
        lib_code = code_prefix + str(code_num)
        picture_path = 'https://img.dlsite.jp/modpub/images2/work/doujin/{lib_code}/{product_code}_img_main.jpg'.format(
            lib_code=lib_code, product_code=code)
    else:
        data = response_object['works'][0]
        cover_url = data['thumb']
        picture_path = cover_url
    picture_response = requests.get(picture_path)
    img = Image.open(BytesIO(picture_response.content), mode='r')
    with BytesIO() as output:
        img.save(output, format='JPEG')
        return output.getvalue()

if __name__ == '__main__':
    code = input_code()
    audio_paths = input_audio_path()

    mainPage = requests.get(
        'https://www.dlsite.com/maniax/work/=/product_id/{code}.html'.format(code=code))
    soup = BeautifulSoup(mainPage.content, 'html.parser')
    workName = soup.find(id="work_name").get_text().replace('\n', '')
    circleName = soup.find(class_="maker_name").get_text().replace('\n', '')
    coverArt = retrive_cover_art(code)

    for audio_path in audio_paths:

        audio = MP3(audio_path, ID3=ID3)

        # adding ID3 tag if it is not present
        try:
            audio.add_tags()
        except error:
            pass

        # edit ID3 tags to open and read the picture from the path specified and assign it
        audio.tags.add(APIC(mime='image/jpeg', type=3, desc=u'Cover',
                            data=coverArt))
        audio.tags.add(TAL(text=workName))
        audio.tags.add(TP1(text=circleName))

        audio.save()  # save the current changes
