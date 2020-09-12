from fastapi import APIRouter
from fastapi.responses import JSONResponse
from modules.status.httpd.httpdStatus import GetHosts, GetModules, GetVersion
from modules.status.waf.wafStatus import EnableCheck

route = APIRouter()

@route.get("/waf")
def wafStatus():
	if EnableCheck() == True:
		return {"enabled": True}
	return {"enabled": False}

@route.get("/httpd/hosts")
def hosts():
	output = GetHosts()
	if output == False:
		return JSONResponse(status_code = 500, content = {"error": "Syntax error"})
	return output

@route.get("/httpd/modules")
def modules():
	output = GetModules()
	if output == False:
		return JSONResponse(status_code = 500, content = {"error": "Syntax error"})
	return output

@route.get("/httpd/version")
def version():
	output = GetVersion()
	if output == False:
		return JSONResponse(status_code = 500, content = {"error": "Syntax error"})
	return {"info": output}