#import youtube_dl
from __future__ import unicode_literals
import csv
import youtube_dl
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip



typeOf = input("Введите тип упражнения: ")
count = int(input("Введите количество видео: "))

SAVE_PATH = os.getcwd() + '/tmp/vidos'
ydl_opts = {
    'outtmpl': SAVE_PATH + '.%(ext)s'
}

with open("countix_train.csv", "r") as f:
    reader = csv.DictReader(f)
    a = list(reader)


i = 0
for elem in a:
    if elem["class"] == typeOf:
        print("gotcha!")
        url = "https://www.youtube.com/watch?v="+elem["video_id"]
        turl = "https://www.youtube.com/watch?v=BaW_jenozKc"
        #print(url)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        start_time = int(elem["kinetics_start"])
        end_time = int(elem["kinetics_end"])
        cwd = os.getcwd()
        try:
            ffmpeg_extract_subclip(cwd + "/tmp/vidos.mp4", start_time, end_time, targetname=cwd + "/push up/test{}.mp4".format(i))
        i = i + 1
        if i >= count:
            break
