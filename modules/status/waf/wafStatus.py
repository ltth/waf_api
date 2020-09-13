import subprocess
from modules.file.dirs.controlDir import ControlDir, CONTROL_DIR_PATH

pathHttpd = CONTROL_DIR_PATH[ControlDir.httpd.value] + "httpd"
pathWAF = CONTROL_DIR_PATH[ControlDir.waf.value] + "modsecurity.conf"

def EnableCheck():
	if b"security2_module" in subprocess.check_output(pathHttpd + " -M | grep 'security2_module'", shell = True):
		return True
	return False

def ModeCheck():
	try:
		output = subprocess.check_output("cat " + pathWAF + " | grep 'SecRuleEngine '", shell = True).decode()
	except:
		return False
	else:
		output = output.split('\n')
		for i in output:
			if len(i) > 13 or i[0] == "#":
				continue
			if " On" in i:
				return "On"
			elif " Off" in i:
				return "Off"
			elif " DetectionOnly" in i:
				return "DetectionOnly"