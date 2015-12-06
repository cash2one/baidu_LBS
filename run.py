#-*- coding:utf-8
import os
import sys
import pdb
import codecs
import time
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
    print "concurrent num:", concurrent
    print "ip num:", len(ip_set)
    KMaxTest = 53
    KStartIndex = 0
    out_put = []
    #ip_set = ip_set[KStartIndex:KStartIndex + KMaxTest]

    concurrency = ConcurrencyBaiduQuery(my_key_set[1], ip_set, concurrent, out_put)
    concurrency.query()

    # sort with original index
    sorted(out_put, key = lambda x : x[0])
    with codecs.open(crawler_name, "wb", "utf-8") as out_stream:
        for bucket_list in out_put:
            for sub_list in bucket_list[1:]:
                for tup in sub_list:
                    out_stream.write(u" ".join(tup) + "\n")
        pass
    pass

def format_seconds(sec):
    if sec < 60:
        return "%d seconds" % sec
    else:
        return "%d minutes %d seconds" % (sec / 60, sec % 60)

def run_with_timer(test, concurrent):
    start_time = time.time()
    test(concurrent)
    end_time = time.time()
    print "time cost:", format_seconds(end_time - start_time)

KDefaultConcurrent = 4
if __name__ == "__main__":
    concurrent = KDefaultConcurrent
    if len(sys.argv) == 2:
        concurrent = int(sys.argv[1])
    run_with_timer(test, concurrent)
