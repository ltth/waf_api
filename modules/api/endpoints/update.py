from fastapi import APIRouter
from fastapi.response import JSONResponse
from modules.file.files.fileAttributes import FileAttributes
from modules.file.dirs.dir import Dir
from os import path

route = APIRouter()

@route.put("/")
def Update(file: FileAttributes):
	path = file.kind.value + file.filename
	if not path.isfile(path):
		return JSONResponse(status_code = 404, content = {"error": "File not found"})
	with open(path, "w") as f:
		size = f.write(file.content)
		return {"path": path, "size": size}