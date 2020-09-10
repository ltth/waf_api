from typing import Optional
from fastapi import APIRouter
from fastapi.response import JSONResponse
from modules.file.dirs.dir import Dir

route = APIRouter()

@route.get("/{kind}/{filename}")
def ViewFile(
	kind: Optional[Dir] = Path(rule, title = "Kind of file"),
	filename: str
):
	try:
		with open(kind.value + filename, "r") as f:
			content = f.read()
	except:
		return JSONResponse(status_code = 404, content = {"error": "File not found"})
	else:
		return {"content": content}