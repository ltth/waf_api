from typing import Optional
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from modules.file.dirs.configDir import CONFIG_DIR_PATH, ConfigDir

route = APIRouter()

@route.get("/{kind}/{filename}")
def ViewFile(
	kind: ConfigDir,
	filename: str
):
	try:
		with open(CONFIG_DIR_PATH[kind.value] + filename, "r") as f:
			content = f.read()
	except:
		return JSONResponse(status_code = 404, content = {"error": "File not found"})
	else:
		return {"content": content}