from __future__ import unicode_literals
import csv
import youtube_dl
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import config


class ConfigData():
    def __init__(self, numberOfVideos, classesList, folderList):
        self.navigator = Navigator()
        self.numberOfVideos = numberOfVideos
        self.classesList = classesList
        self.folderList = folderList
        self.cwd = os.getcwd()
        self.navigator.createFolder("Downloads", "")
        self.classesDict = dict()
        for elem in self.folderList:
            try:
                self.getClassList(elem)
            except NameError:
                print("wrong name in the config, buddy!")

    def getClassList(self, folderName):
        self.navigator.createFolder(folderName, "Downloads")
        with open("countix_{}.csv".format(folderName), "r") as f:
            reader = csv.DictReader(f)
            if folderName == "train":
                self.train = list(reader)
                self.classesDict["train"] = self.train
                print('Added {} elements to classesDict["{}"]'.format(
                    len(self.train), folderName))

            elif folderName == "val":
                self.val = list(reader)
                self.classesDict["val"] = self.val
                print('Added {} elements to classesDict["{}"]'.format(
                    len(self.val), folderName))
            elif folderName == "test":
                self.test = list(reader)
                self.classesDict["test"] = self.test
                print('Added {} elements to classesDict["{}"]'.format(
                    len(self.test), folderName))
            else:
                raise NameError(
                    'Got {}, exected ["train","eval","test"]'.format(folderName))


class DownloadLogic():
    def __init__(self, configDataObj):
        self.navigator = Navigator()
        #self.classesDict = configDataObj.classesDict
        self.configDataObj = configDataObj
        self.cwd = configDataObj.cwd
        SAVE_PATH = os.getcwd() + '/tmp/vidos'
        self.ydl_opts = {
            'outtmpl': SAVE_PATH + '.%(ext)s'
        }
        self.getAllFolders()

    def getAllFolders(self):
        for elem in self.configDataObj.folderList:
            self.getAllClasses(elem)

    def getAllClasses(self, folderName):
        for elem in self.configDataObj.classesList:
            self.navigator.createFolder(elem, "/Downloads/{}".format(folderName))
            self.getVideos(folderName, elem)

    def getVideos(self, folderName, className):
        count = 0
        for i in range(len(self.configDataObj.classesDict[folderName])):
            meta = VideoMeta(self.configDataObj, i, folderName)
            if meta.isValidClass(className):
                self.downloadVideo(id, className, folderName, i, meta)
                count = count + 1
            if count >= self.configDataObj.numberOfVideos:
                break

    def downloadVideo(self, id, className, folder, index, meta):
        self.cwd = self.configDataObj.cwd
        self.videometa = meta
        print(self.videometa.classname, className)
        if self.videometa.isValidClass(className):
            print("gotcha!")
            url = "https://www.youtube.com/watch?v="+self.videometa.id
            turl = "https://www.youtube.com/watch?v=BaW_jenozKc"
            # print(url)
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                try:
                    ydl.download([url])
                    self.clipVideo(folder, index)
                except youtube_dl.utils.ExtractorError:
                    print("oops!")
                except youtube_dl.utils.DownloadError:
                    arr = os.listdir(self.cwd + "/tmp/")
                    for elem in arr:
                        os.remove(self.cwd + "/tmp/" + elem)

    def clipVideo(self, folder, index):
        arr = os.listdir(self.cwd + "/tmp/")
        elem = arr[0]
        if folder == "train" or folder == "val":
            if "mp4" in elem:
                ffmpeg_extract_subclip(self.cwd + "/tmp/vidos.mp4", self.videometa.start_time,
                                       self.videometa.end_time, targetname=self.cwd + "/Downloads/{}/{}/test{}.mp4".format(folder, self.videometa.classname, index))
            elif "mkv" in elem:
                ffmpeg_extract_subclip(self.cwd + "/tmp/vidos.mkv", self.videometa.start_time, self.videometa.end_time,
                                       targetname=self.cwd + "/Downloads/{}/{}/test{}.mkv".format(folder, self.videometa.classname, index))
        else:
            if "mp4" in elem:
                ffmpeg_extract_subclip(self.cwd + "/tmp/vidos.mp4", self.videometa.start_time,
                                       self.videometa.end_time, targetname=self.cwd + "/Downloads/{}/test{}.mp4".format(folder, index))
            elif "mkv" in elem:
                ffmpeg_extract_subclip(self.cwd + "/tmp/vidos.mkv", self.videometa.start_time, self.videometa.end_time,
                                       targetname=self.cwd + "/Downloads/{}/test{}.mkv".format(folder, index))
        os.remove(self.cwd + "/tmp/" + elem)


class VideoMeta():
    def __init__(self, configDataObj, index, folder):
        row = configDataObj.classesDict[folder][index]
        self.folder = folder
        try:
            self.classname = row["class"]
        except KeyError:
            self.classname = "test"
        self.id = row["video_id"]
        self.start_time = int(row["kinetics_start"])
        self.end_time = int(row["kinetics_end"])
        print("got meta for index {}, with id: {} , {}, {}".format(
            index, self.id, self.start_time, self.end_time))

    def isValidClass(self, inclassname):
        return inclassname == self.classname or self.folder == "test"


class Navigator():
    def __init__(self):
        self.cwd = os.getcwd()
        print("========================")
        print(self.cwd)

    def createFolder(self, name, level):
        if len(level) >= 0:
            self.cwd = os.getcwd() + "/{}/".format(level)
            print(self.cwd + "{}".format(name))
            print("========================")
        try:
            os.mkdir(self.cwd+"/{}".format(name))
            print("Created the {} folder".format(name))
        except FileExistsError:
            print("mybad, folder {} already there".format(name))
        if len(level) >= 0:
            self.cwd = self.cwd[: 1-len(level)]
