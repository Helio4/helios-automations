import os
from youtube_dl import YoutubeDL

if __name__ == '__main__':
    video_url = input('Enter the video URL: ')
    ydl_opts = {
        'format': '299+140'
    }
    video_info = YoutubeDL(ydl_opts).extract_info(video_url, download=False)
    video_true_url = video_info['requested_formats'][0]['url']
    audio_true_url = video_info['requested_formats'][1]['url']

    start_time = input('Enter the starting time (if any): ')
    end_time = input('Enter the ending time (if any): ')

    input_options = ''
    if start_time != '':
        input_options += "-ss " + start_time + " "
    if end_time != '':
        input_options += "-to " + end_time + " "

    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    os.system("ffmpeg " + input_options + "-i \"" + video_true_url + "\" " + input_options + "-i \"" +
              audio_true_url + "\" -map 0:v -map 1:a -ss 30 -c:v libx264 -preset ultrafast -crf 19 -c:a copy " + video_info['id'] + ".mp4")
