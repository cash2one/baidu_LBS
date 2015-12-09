#-*- coding:utf-8
import os
import sys
import pdb
import codecs
import time
import multiprocessing
from process_based_query import process_based_query

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
                print "current index:", index
        with open(crawler_name, "wb") as out_stream:
            out_stream.writelines(write_buffer)
            pass
        pass
    pass


def test(concurrent_coroutines, test_len=0):
    ip_set = read_ip_set()
    KMaxTest = 80000
    KStartIndex = 0
    out_put = []
    if test_len:
        ip_set = ip_set[KStartIndex:KStartIndex + test_len]

    print "ip num:", len(ip_set)
    print "concurrent coroutines num:", concurrent_coroutines

    process_based_query(my_key_set[0],
                        concurrent_coroutines,
                        ip_set,
                        out_put)
    print "query done, now sorting"
    sorted(out_put, key=lambda x: x[0])

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


def run_with_timer(test, concurrent, test_set_len):
    start_time = time.time()
    test(concurrent, test_set_len)
    end_time = time.time()
    print "time cost:", format_seconds(end_time - start_time)

KDefaultConcurrent = 30
if __name__ == "__main__":
    concurrent = KDefaultConcurrent
    test_set_len = 0
    if len(sys.argv) >= 2:
        concurrent = int(sys.argv[1])
    if len(sys.argv) == 3:
        test_set_len = int(sys.argv[2])
    run_with_timer(test, concurrent, test_set_len)
