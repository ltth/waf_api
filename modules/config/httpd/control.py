import os
from modules.file.dirs.controlDir import ControlDir

path = ControlDir.httpd.value + "apachectl"

def Start():
	os.system(path + " -k start")

def Restart():
	os.system(path + " -k graceful")

def Stop():
	os.system(path + " -k gracefule-stop")