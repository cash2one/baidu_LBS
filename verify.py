import os
import sys

dict_name = "../qqwry-daemon/out.txt"
query_res_name = "baidu_res.txt"


def read_set(fname):
    ip_set = []
    with open(fname, "r") as input_stream:
        ip_set.extend([line.split(' ')[0] for line in input_stream])
    return ip_set


def read_dict_set():
    return read_set(dict_name)


def read_query_set():
    return read_set(query_res_name)


def main():
    dict_set = read_dict_set()
    query_set = read_query_set()

    if not len(dict_set) == len(query_set):
        print ("line count error, dict len:",
               len(dict_set), ",query len:",
               len(query_set))
        return
    if not dict_set == query_set:
        print "content not equal"
        return
    print "file content exactly equal"
    return

if __name__ == "__main__":
    main()
