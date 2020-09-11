import os
from modules.file.dirs.controlDir import ControlDir

path = ControlDir.httpd.value + "httpd"

def CheckSyntax():
	return (os.system(path + " -t") == 0)

def 