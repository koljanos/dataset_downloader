#import youtube_dl
from __future__ import unicode_literals
import csv
import youtube_dl
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import config



typeOf = config.spisok
count = config.number
folderList = config.folders

SAVE_PATH = os.getcwd() + '/tmp/vidos'
ydl_opts = {
    'outtmpl': SAVE_PATH + '.%(ext)s'
}

with open("countix_train.csv", "r") as f:
    reader = csv.DictReader(f)
    a = list(reader)

for folder in folderList:
    for upraj in typeOf:


i = 0
for elem in a:
    if elem["class"] == typeOf:
        print("gotcha!")
        url = "https://www.youtube.com/watch?v="+elem["video_id"]
        turl = "https://www.youtube.com/watch?v=BaW_jenozKc"
        #print(url)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([url])
                start_time = int(elem["kinetics_start"])
                end_time = int(elem["kinetics_end"])
                cwd = os.getcwd()
                arr = os.listdir(cwd + "/tmp/")
                elem = arr[0]
                if "mp4" in elem :
                    ffmpeg_extract_subclip(cwd + "/tmp/vidos.mp4", start_time, end_time, targetname=cwd + "/push up/test{}.mp4".format(i))
                elif "mkv" in elem :
                    ffmpeg_extract_subclip(cwd + "/tmp/vidos.mkv", start_time, end_time, targetname = cwd + "/push up/test{}.mkv".format(i))
                os.remove(cwd + "/tmp/" + elem)
            except youtube_dl.utils.ExtractorError:
                print("oops!")
            except youtube_dl.utils.DownloadError:
                cwd = os.getcwd()
                arr = os.listdir(cwd + "/tmp/")
                for elem in arr:
                    os.remove(cwd + "/tmp/" + elem)


        i = i + 1
        if i >= count:
            break
