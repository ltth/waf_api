from enum import Enum

class ConfigDir(str, Enum):
	rule = "rule"
	rule_config = "rule_config"
	waf_config = "waf_config"
	httpd = "httpd"
	proxy = "proxy"

DIR_PATH = {
	"rule": "/rule/rules/",
	"rule_config": "/rule/",
	"waf_config": "/waf/",
	"httpd": "/httpd/",
	"proxy": "/proxy/"
}