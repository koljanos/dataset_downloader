import os


class Navigator():
    def __init__(self):
        self.cwd = os.getcwd()
    def createFolder(self, name, level):
        if len(level) >= 0:
            self.cwd = self.cwd + "{}/".format(level)
            print(self.cwd, self.cwd+"{}/".format(name))
        try:
            os.mkdir(self.cwd+"{}/".format(name))
            print("Created the {} folder".format(name))
        except FileExistsError:
            print("mybad, folder {} already there".format(name))
        if len(level) >= 0:
            self.cwd = self.cwd[: -len(level)]

navigator = Navigator()
navigator.createFolder("Downloads","")
navigator.createFolder("test","Downloads")

def convert_avi_to_mp4(avi_file_path, output_name):
    os.popen("ffmpeg -i '{input}' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 '{output}.mp4'".format(
        input=avi_file_path, output=output_name))
    return True

