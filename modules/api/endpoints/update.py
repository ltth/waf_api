from fastapi import APIRouter
from fastapi.responses import JSONResponse
from modules.file.files.fileAttributes import FileAttributes
from modules.file.dirs.dir import DIR_PATH
from os import path

route = APIRouter()

@route.put("/")
def Update(file: FileAttributes):
	path = DIR_PATH[file.kind.value] + file.filename
	if not path.isfile(path):
		return JSONResponse(status_code = 404, content = {"error": "File not found"})
	with open(path, "w") as f:
		size = f.write(file.content)
		return {"path": path, "size": size}