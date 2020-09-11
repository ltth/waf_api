from enum import Enum

class ControlDir(str, Enum):
	waf_config = "waf_config"
	httpd = "httpd"

DIR_PATH = {
	"waf_config": "/waf/",
	"httpd": "/httpd/"
}