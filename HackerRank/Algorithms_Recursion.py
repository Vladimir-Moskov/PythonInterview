######################################################################
# https://www.hackerrank.com/challenges/the-power-sum/problem
# The Power Sum
#
# import math
#
#
# def powerSum(X, N):
#     x_root_n = (math.po(X)) + 1
#     arr_2 = [0] * x_sqrt
#     arr_sum = [0] * x_sqrt
#
#     for i in range(x_sqrt):
#         arr_2[i] = i * i
#
#     for i in range(0, N):
#         k = 1
#         while arr_sum[k] <= X:
#             arr_sum[k] =



















def n_uniq_max(given_list, n):
    if n > len(given_list):
        return 0

    val_list = list(set(given_list))
    val_list.sort()

    result = sum(val_list[-n:])

    return result


def n_uniq_max_2(given_list, n):
    if n > len(given_list):
        return 0

    val_dic = {key: 0 for key in given_list}

    if n > len(val_dic.keys()):
        n = len(val_dic.keys())

    max_list = list(val_dic.keys())[:n]
    current_min = max_list[0]
    for val in max_list:
        if current_min > val:
            current_min = val

    for key in list(val_dic.keys())[n:]:
        if key > current_min:
            for i in range(len(max_list)):
                if max_list[i] == current_min:
                    max_list[i] = key

            current_min = max_list[0]
            for val in max_list:
                if current_min > val:
                    current_min = val

    result = 0
    for val in max_list:
        result += val

    return result


import time

def timeit(temed):

    def decorted(*args, **kargs):
        start_time = time.perf_counter()
        result = temed(*args, **kargs)
        print(f"Execution_time = {time.perf_counter() - start_time} ms")
        return result

    decorted.__name__ = temed.__name__
    return decorted


@timeit
def fibonachi(n):
    if n < 2:
        return n

    result = 1
    prev = 0
    current = 1
    for i in range(2, n + 1):
        prev, current = current, prev + current
        result += current

    return result

print(fibonachi(100))


# print(n_uniq_max_2( [1,2,3,7,23,99,1,2,4,1,15,6,4,99], 3))



















