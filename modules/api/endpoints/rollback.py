from fastapi import APIRouter
from modules.file.files.fileAttributes import FileAttributes
from modules.file.dirs.configDir import CONFIG_DIR_PATH

route = APIRouter()

@route.put("/")
def Rollback(file: FileAttributes):
	path = CONFIG_DIR_PATH[file.kind.value] + file.filename
	with open(path, "w") as f:
		size = f.write(file.content)
		return {"path": path, "size": size}