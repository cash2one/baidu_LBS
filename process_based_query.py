import multiprocessing
import pdb
import math


def process_based_query(
        token_key,
        per_core_coroutines,
        ip_set,
        result_list,
        process_num=multiprocessing.cpu_count()):
    process_pool = multiprocessing.Pool(process_num)
    print "process num:", process_num

    ip_set_len = len(ip_set)
    per_process_set_len = int(math.ceil(1.0 * ip_set_len / process_num))

    arg_list = []
    for i in xrange(process_num):
        index_begin = i * per_process_set_len
        index_end = index_begin + per_process_set_len
        if index_end > ip_set_len:
            index_end = ip_set_len
        arg_list.append([i, token_key, per_core_coroutines,
                         ip_set[index_begin:index_end]])
    result_list.extend(process_pool.map(query_wrapper, arg_list))
    print "process pool process done!"


def query_wrapper(args):
    return do_query(*args)


def do_query(index, token_key, per_core_coroutines, ip_set):
    from concurrency_baidu_query import ConcurrencyBaiduQuery
    part_result_list = []
    concurrency_query = ConcurrencyBaiduQuery(
        index,
        token_key,
        ip_set,
        per_core_coroutines,
        part_result_list)
    concurrency_query.query()

    return part_result_list
