from fastapi import APIRouter
from modules.config.httpd.httpdControl import *
import os

route = APIRouter()

@route.get("/start")
def Start():
	Start()
	return {}

@route.get("/restart")
def Start():
	Restart()
	return {}

@route.get("/stop")
def Start():
	Stop()
	return {}