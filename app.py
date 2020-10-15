import youtube_dl
import csv

typeOf = input("Введите тип упражнения:")
count = int(input("Введите количество видео"))

with open("countix_train.csv", "r") as f:
    reader = csv.DictReader(f)
    a = list(reader)


i = 0
for elem in a:
    if elem["class"] == typeOf:
        print("gotcha!")
        url = "https://www.youtube.com/watch?v="+elem["video_id"]
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        i = i + 1
        if i >= count:
            break
