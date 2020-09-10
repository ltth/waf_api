from fastapi import APIRouter
from modules.file.files.fileAttributes import FileAttributes
from modules.file.dirs.dir import DIR_PATH
from os import path

route = APIRouter()

@route.post("/")
def AddFile(file: FileAttributes):
	path = DIR_PATH[file.kind.value] + file.filename
	if path.isfile(path):
		return {"error": "File existed"}
	with open(path, "w") as f:
		size = f.write(file.content)
		return {"path": path, "size": size}