from fastapi import APIRouter
from fastapi.responses import JSONResponse
from modules.status.httpd.httpdStatus import GetHosts, GetModules, GetVersion, GetStatus
from modules.status.waf.wafStatus import EnableCheck, ModeCheck

route = APIRouter()

@route.get("/waf", tags = ["waf"])
def wafStatus():
	output = ModeCheck()
	if output == False:
		return JSONResponse(status_code = 500, content = {"error": "Can not find SecRuleEngine mode"})
	return {"mode": output}

@route.get("/waf/enable", tags = ["waf"])
def CheckEnable():
	if EnableCheck() == True:
		return {"enabled": True}
	return {"enabled": False}

@route.get("/httpd", tags = ["httpd"])
def httpdStatus():
	output = GetStatus()
	if output == False:
		return {"status": "Not active"}
	return {"status": "Active", "pid": output}

@route.get("/httpd/hosts", tags = ["httpd"])
def hosts():
	output = GetHosts()
	if output == False:
		return JSONResponse(status_code = 500, content = {"error": "Syntax error"})
	return output

@route.get("/httpd/modules", tags = ["httpd"])
def modules():
	output = GetModules()
	if output == False:
		return JSONResponse(status_code = 500, content = {"error": "Syntax error"})
	return output

@route.get("/httpd/version", tags = ["httpd"])
def version():
	output = GetVersion()
	if output == False:
		return JSONResponse(status_code = 500, content = {"error": "Syntax error"})
	return {"info": output}