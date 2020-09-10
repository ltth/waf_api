from fastapi import APIRouter
from modules.file.files.fileAttributes import FileAttributes
from modules.file.dirs.dir import DIR_PATH
import os

route = APIRouter()

@route.delete("/")
def AddFile(file: FileAttributes):
	try:
		os.remove(DIR_PATH[file.kind.value] + file.filename)
	except:
		pass
	finally:
		return {}