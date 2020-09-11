from enum import Enum

class ControlDir(str, Enum):
	# waf_config = "waf_config"
	httpd = "httpd"
	httpd_log = "httpd_log"

CONTROL_DIR_PATH = {
	# "waf_config": "/usr/local/apache2/conf/extra/",
	"httpd": "/usr/local/apache2/bin/",
	"httpd_log": "/usr/local/apache2/logs/"
}