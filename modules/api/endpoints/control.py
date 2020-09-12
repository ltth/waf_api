from fastapi import APIRouter
from fastapi.responses import JSONResponse
from modules.config.httpd.httpdControl import Start, Restart, Stop

route = APIRouter()

@route.get("/start")
def start():
	if Start() != True:
		return JSONResponse(status_code = 500, content = {"error": "Syntax error"})
	return {}

@route.get("/restart")
def restart():
	if Restart() != True:
		return JSONResponse(status_code = 500, content = {"error": "Syntax error"})
	return {}

@route.get("/stop")
def stop():
	if Stop() != True:
		return JSONResponse(status_code = 500, content = {"error": "Syntax error"})
	return {}