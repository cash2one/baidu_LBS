import json
import requests


class BaiduQuery:
    GRUL = "http://api.map.baidu.com/location/ip?ak="
    IP_SPLITTER = "&ip="
    JSON_KEY_EXTRACT = "address"

    def __init__(self, key):
        self.key_ = key
        self.session_ = requests.Session()

    def get_addr(self, ip_str):
        get_result = self.session_.get(self.build_url(ip_str))
        try:
            json_data = json.loads(get_result.text)
            return json_data[self.JSON_KEY_EXTRACT]
        except:
            return "UNKNOWN"

    def build_url(self, ip_str):
        return self.GRUL + self.key_ + self.IP_SPLITTER + ip_str
