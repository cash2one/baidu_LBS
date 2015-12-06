#-*- coding:utf-8
import os
import sys
import pdb
import codecs
from time import ctime
from baidu_query import BaiduQuery
from concurrency_baidu_query import ConcurrencyBaiduQuery

dict_name = "../qqwry-daemon/out.txt"
crawler_name = "baidu_res.txt"
my_key_set = [
    "TbS84y8GLtHCXBZyGbPe9ICH",
    "pEjA6Amc6rVtO6nPqkEBdtVL",
    "UKdMdIi0rqOYPqecY8rxjGG5",
    "CbBRkw8K9Yv1g8c0Gr8qaIGa"
]

def read_ip_set():
    ip_set = []
    with open(dict_name, "r") as input_stream:
        ip_set.extend([line.split(' ')[0] for line in input_stream])
    return ip_set

def main():
    write_buffer = []
    index = 0
    ip_set = []
    with open(dict_name, "r") as input_stream:
        ip_set.extend([line.split(' ')[0] for line in input_stream])
        for ip in ip_set:
            query = BaiduQuery(my_key_set[0], ip)
            write_buffer.append(u" ".join(query.get_addr()) + "\n")
            index += 1
            if index % 100 == 0:
                print "current index:" ,index
        with open(crawler_name, "wb") as out_stream:
            out_stream.writelines(write_buffer)
            pass
        pass
    pass

def test(concurrent):
    ip_set = read_ip_set()
    KMaxTest = 50000
    KStartIndex = 1000
    out_put = []
    #ip_set = ip_set[KStartIndex:KStartIndex + KMaxTest]

    print ctime()
    concurrency = ConcurrencyBaiduQuery(my_key_set[0], ip_set, concurrent, out_put)
    concurrency.query()
    print ctime()

    with codecs.open(crawler_name, "wb", "utf-8") as out_stream:
        for tup in out_put:
            out_stream.write(u" ".join(tup) + "\n")
        #out_stream.writelines([(u" ".join(tup) + u"\n") for tup in out_put])
        pass
    print ctime()

KDefaultConcurrent = 4
if __name__ == "__main__":
    concurrent = KDefaultConcurrent
    if len(sys.argv) == 2:
        concurrent = int(sys.argv[1])
    print "concurrent num:", concurrent
    test(concurrent)
