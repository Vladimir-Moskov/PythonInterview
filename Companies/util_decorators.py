"""
    Put here some decorators for general usage

"""


def timeit(method):
    """
        execution time decorator
         may be useful to validate performance of a solution
    :param method:
    :return:
    """
    def timed(*args, **kw):
        # local import, bad practice but good way to import source only in place where you really need it
        import time
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' %
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed

from collections import Counter


def solution(arr, int_val):
    return Counter(arr)[int_val]

print(solution([1, 2, 3, 1], 1))