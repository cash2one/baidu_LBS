#-*- coding:utf-8
import os
import sys
import pdb
import codecs
import gevent
from gevent.queue import Queue
from baidu_query import *
from gevent import monkey
monkey.patch_socket()

task_queue = Queue()

dict_name = "qqwry_ip_dict.in"
crawler_name = "baidu_res.txt"
my_key_set = [
    "TbS84y8GLtHCXBZyGbPe9ICH",
    "pEjA6Amc6rVtO6nPqkEBdtVL",
    "UKdMdIi0rqOYPqecY8rxjGG5",
    "CbBRkw8K9Yv1g8c0Gr8qaIGa"
]

g_running = True
def read_ip_set():
    ip_set = []
    with open(dict_name, "r") as input_stream:
        for line in input_stream:
            task_queue.put(line.split(' ')[0])

def worker(i):
    print "enter worker:", i
    queryer = BaiduQuery(my_key_set[0])
    while g_running and not task_queue.empty():
        ip = task_queue.get()
        x = queryer.get_addr(ip)
        pass
    pass

gevent.spawn(read_ip_set).join()
jobs = [gevent.spawn(worker, i) for i in xrange(200)]
gevent.wait(jobs)
g_running = False
