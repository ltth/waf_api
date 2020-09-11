from fastapi import APIRouter
from modules.file.files.fileAttributes import FileAttributes
from modules.file.dirs.configDir import CONFIG_DIR_PATH
import os

route = APIRouter()

@route.delete("/")
def AddFile(file: FileAttributes):
	try:
		os.remove(CONFIG_DIR_PATH[file.kind.value] + file.filename)
	except:
		pass
	finally:
		return {}