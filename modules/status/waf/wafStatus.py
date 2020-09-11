import subprocess
from modules.file.dirs.controlDir import ControlDir, CONTROL_DIR_PATH

path = CONTROL_DIR_PATH[ControlDir.httpd.value] + "httpd"

def EnableCheck():
	if b"security2_module" in subprocess.check_output(path + " -M | grep 'security2_module'", shell = True):
		return True
	return False