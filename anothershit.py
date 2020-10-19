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