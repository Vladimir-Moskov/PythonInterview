######################################################################
# https://www.hackerrank.com/challenges/the-power-sum/problem
# The Power Sum

import math


def powerSum(X, N):
    x_root_n = (math.po(X)) + 1
    arr_2 = [0] * x_sqrt
    arr_sum = [0] * x_sqrt

    for i in range(x_sqrt):
        arr_2[i] = i * i

    for i in range(0, N):
        k = 1
        while arr_sum[k] <= X:
            arr_sum[k] =