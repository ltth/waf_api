from fastapi import APIRouter
from modules.file.files.fileAttributes import FileAttributes
from os

route = APIRouter()

@route.delete("/")
def AddFile(file: FileAttributes):
	try:
		os.remove(file.kind.value + file.filename)
	except:
		pass
	finally:
		return {}