import subprocess, os, re
from modules.file.dirs.controlDir import ControlDir, CONTROL_DIR_PATH

path = CONTROL_DIR_PATH[ControlDir.httpd.value] + "httpd"

def CheckSyntax():
	return (os.system(path + " -t") == 0)

def GetHosts():
	if CheckSyntax() != True:
		return False
	regex = "\:(\d+(?!\)))\s+([\da-z-A-Z\.]+)\s*\((.+)\)"
	output = subprocess.check_output(path + " -t -D DUMP_VHOSTS", shell = True).decode()
	result = re.findall(regex, output)
	hosts = []
	for port, hostname, position in result:
		hosts.append({"port": port, "hostname": hostname, "define-position": position})
	return hosts

def GetModules():
	if CheckSyntax() != True:
		return False
	regex = "\s*(.+)\s\(([a-z]+)\)"
	output = subprocess.check_output(path + " -M", shell = True).decode()
	output = output.split("\n")[1:-1]
	modules = []
	for i in output:
		if "(" not in i or ")" not in i:
			continue
		moduleName, status = re.findall(regex, i)[0]
		modules.append({"name": moduleName, "status": status})
	return modules

def GetVersion():
	if CheckSyntax():
		return subprocess.check_output(path + " -v", shell = True).decode()
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