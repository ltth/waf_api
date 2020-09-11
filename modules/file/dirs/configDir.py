from enum import Enum

class ConfigDir(str, Enum):
	rule = "rule"
	rule_config = "rule_config"
	waf_config = "waf_config"
	httpd = "httpd"
	proxy = "proxy"

DIR_PATH = {
	"rule": "/opt/waf/crs-rules/rules/",
	"rule_config": "/opt/waf/crs-rules/",
	"waf_config": "/usr/local/apache2/conf/extra/",
	"httpd": "/usr/local/apache2/conf/",
	"proxy": "/usr/local/apache2/conf/sites-enabled/"
}