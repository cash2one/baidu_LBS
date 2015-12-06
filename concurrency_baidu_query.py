import gevent
from gevent import monkey
monkey.patch_all()
import math
from time import ctime
from baidu_query import BaiduQuery

class ConcurrencyBaiduQuery:

    def __init__(self, key, ip_set, concurrency_num, out_list):
        self.key_ = key
        self.ip_set_ = ip_set
        self.max_index_ = len(ip_set)
        self.num_ = concurrency_num
        self.bucket_len_ = int(math.ceil(1.0 * len(ip_set) / concurrency_num))
        self.out_put_ = out_list
        pass

    def query(self):
        print "ip num for query:", self.max_index_
        jobs = [gevent.spawn(self.do_query, i) for i in xrange(self.num_)]
        gevent.wait(jobs)
        pass

    def do_query(self, index):
        start_index = index * self.bucket_len_
        end_index = start_index + self.bucket_len_
        ## deal with divide remain
        if end_index >= self.max_index_:
            end_index = self.max_index_
            pass
        cnt = 0
        baidu_query = BaiduQuery(self.key_)
        # temp output list
        tmp_result = []
        for i in xrange(start_index, end_index):
            current_ip = self.ip_set_[i]
            tmp_result.append((current_ip, baidu_query.get_addr(self.ip_set_[i])))
            cnt += 1
            if cnt % 1000 == 0:
                print "index:", index, ",sub index:", cnt, ctime()
                pass
            pass
        self.out_put_.append([index, tmp_result])
        pass
