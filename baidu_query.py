import urllib2
import json

class BaiduQuery:
	GRUL = "http://api.map.baidu.com/location/ip?ak="
	IP_SPLITTER = "&ip="
	JSON_KEY_EXTRACT = "address"

	def __init__(self, key, ip_str):
		self.key_ = key
		self.ip_ = ip_str
	def get_addr(self):
		url = urllib2.urlopen(self.build_url())
		content = url.read()
		json_data = json.loads(content)
		try:
			return (self.ip_, json_data[self.JSON_KEY_EXTRACT])
		except:
			return (self.ip_, "UNKNOWN")
	def build_url(self):
		return self.GRUL + self.key_ + self.IP_SPLITTER + self.ip_
