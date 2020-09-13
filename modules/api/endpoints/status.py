from fastapi import APIRouter
from fastapi.responses import JSONResponse
from modules.status.httpd.httpdStatus import GetHosts, GetModules, GetVersion, GetStatus
from modules.status.waf.wafStatus import EnableCheck, ModeCheck

route = APIRouter()

@route.get("/waf", tags = ["waf status"])
def wafStatus():
	output = ModeCheck()
	if output == False or output is None :
		return JSONResponse(status_code = 500, content = {"error": "Can not find SecRuleEngine mode"})
	return {"mode": output}

@route.get("/waf/enable", tags = ["waf status"])
def CheckEnable():
	if EnableCheck() == True:
		return {"enabled": True}
	return {"enabled": False}

@route.get("/httpd", tags = ["httpd status"])
def httpdStatus():
	output = GetStatus()
	if output == False:
		return {"status": "Not active"}
	return {"status": "Active", "pid": output}

@route.get("/httpd/hosts", tags = ["httpd status"])
def hosts():
	output = GetHosts()
	if output == False:
		return JSONResponse(status_code = 500, content = {"error": "Syntax error"})
	return output

@route.get("/httpd/modules", tags = ["httpd status"])
def modules():
	output = GetModules()
	if output == False:
		return JSONResponse(status_code = 500, content = {"error": "Syntax error"})
	return output

@route.get("/httpd/version", tags = ["httpd status"])
def version():
	output = GetVersion()
	if output == False:
		return JSONResponse(status_code = 500, content = {"error": "Syntax error"})
	return {"info": output}