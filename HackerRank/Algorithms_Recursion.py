######################################################################
# https://www.hackerrank.com/challenges/the-power-sum/problem
# The Power Sum
#

import math


def powerSum(X, N):
    result = 0
    x_root_n = int(X ** (1 / N))
    arr_pow_n = [0] * (x_root_n + 1)

    for i in range(x_root_n + 1):
        arr_pow_n[i] = i ** N

    result = check_val(arr_pow_n, 1, X)

    return result

def check_val(arr, cur_index, cur_val):
    result = 0
    if cur_index < len(arr):
        for i in range(cur_index, len(arr)):
            if arr[i] == cur_val:
                result += 1
                break
            elif arr[cur_index] > cur_val:
                break
            else:
                result += check_val(arr, i + 1, cur_val - arr[i])
    return result



print(powerSum(10, 2))  # 1
print(powerSum(100, 2))  # 3
print(powerSum(100, 3))  # 1

######################################################################
























