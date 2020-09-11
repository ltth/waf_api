from fastapi import APIRouter
from modules.config.httpd.httpdControl import Start, Restart, Stop

route = APIRouter()

@route.get("/start")
def start():
	Start()
	return {}

@route.get("/restart")
def restart():
	Restart()
	return {}

@route.get("/stop")
def stop():
	Stop()
	return {}