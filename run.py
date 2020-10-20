from dataset_downloader import ConfigData, DownloadLogic, VideoMeta
import config

numberOfVideos = config.number
classesList = config.spisok
folderList = config.folders

session = ConfigData(numberOfVideos ,classesList ,folderList)
download = DownloadLogic(session) [::]