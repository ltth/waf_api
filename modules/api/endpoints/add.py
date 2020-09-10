from fastapi import APIRouter
from modules.file.files.fileAttributes import FileAttributes
from os import path

@route.post("/")
def AddFile(file: FileAttributes):
	path = file.kind.value + file.filename
	if path.isfile(path):
		return {"error": "File existed"}
	with open(path, "w") as f:
		size = f.write(file.content)
		return {"path": path, "size": size}