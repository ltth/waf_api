from fastapi import APIRouter
from fastapi.responses import JSONResponse
from modules.file.files.fileAttributes import FileAttributes
from modules.file.dirs.configDir import CONFIG_DIR_PATH
import os

route = APIRouter()

@route.put("/")
def Update(file: FileAttributes):
	path = CONFIG_DIR_PATH[file.kind.value] + file.filename
	if not os.path.isfile(path):
		return JSONResponse(status_code = 404, content = {"error": "File not found"})
	with open(path, "w") as f:
		size = f.write(file.content)
		return {"path": path, "size": size}