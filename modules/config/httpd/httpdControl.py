import os
from modules.file.dirs.controlDir import ControlDir

path = ControlDir.httpd.value + "httpd"

def Start():
	return (os.system(path + " -k start") == 0)

def Restart():
	return (os.system(path + " -k graceful") == 0)

def Stop():
	return (os.system(path + " -k graceful-stop") == 0)