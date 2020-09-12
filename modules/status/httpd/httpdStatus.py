import subprocess
import os
from modules.file.dirs.controlDir import ControlDir, CONTROL_DIR_PATH

path = CONTROL_DIR_PATH[ControlDir.httpd.value] + "httpd"

def CheckSyntax():
	return (os.system(path + " -t") == 0)

def GetHosts():
	if CheckSyntax():
		return subprocess.check_output(path + " -t -D DUMP_VHOSTS", shell = True)
	else:
		return False

def GetModules():
	if CheckSyntax():
		return subprocess.check_output(path + " -M", shell = True)
	else:
		return False

def GetVersion():
	if CheckSyntax():
		return subprocess.check_output(path + " -v", shell = True)
	else:
		return False

def GetStatus():
	try:
		with open(CONTROL_DIR_PATH[ControlDir.httpd_log.value] + "httpd.pid", "r") as f:
			pid = f.read()
	except:
		return False
	else:
		return int(pid)