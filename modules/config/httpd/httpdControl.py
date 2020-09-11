import os
from modules.file.dirs.controlDir import ControlDir, CONTROL_DIR_PATH
from modules.status.httpd.httpdStatus import CheckSyntax, GetStatus

path = CONTROL_DIR_PATH[ControlDir.httpd.value] + "httpd"

def Start():
	if not GetStatus():
		if CheckSyntax():
			return (os.system(path + " -k start") == 0)
		return False
	Restart()

def Restart():
	if GetStatus():
		if CheckSyntax():
			return (os.system(path + " -k graceful") == 0)
		return False
	Start()

def Stop():
	if GetStatus():
		if CheckSyntax():
			return (os.system(path + " -k graceful-stop") == 0)
		return False
	return True