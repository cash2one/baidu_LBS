#!/usr/bin/python
#-*- coding:utf-8

import urllib2
import codecs
import json
import sys

GURL = "http://api.map.baidu.com/location/ip?ak=CbBRkw8K9Yv1g8c0Gr8qaIGa&ip=217.13.228.160&coor=bd09ll"


def main():
    f = urllib2.urlopen(GURL)
    content = f.read()
    json_data = json.loads(content)
    s = json.dumps(json_data, sort_keys=True, indent=4, separators=(',', ': '))
    print json_data["message"]
    print s
    return

    # with codecs.open("out.txt", "wb", "utf-8") as out_stream:
    with open("out.txt", "wb") as out_stream:
        json.dump(
            json_data,
            out_stream,
            sort_keys=True,
            indent=4,
            separators=(
                ',',
                ': '))
    pass

if __name__ == "__main__":
    main()
