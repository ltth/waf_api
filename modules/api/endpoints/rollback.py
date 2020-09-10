from fastapi import APIRouter
from modules.file.files.fileAttributes import FileAttributes

route = APIRouter()

@route.put("/")
def Rollback(file: FileAttributes):
	path = file.kind.value + file.filename
	with open(path, "w") as f:
		size = f.write(file.content)
		return {"path": path, "size": size}