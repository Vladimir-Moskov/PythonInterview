# AlgorithmsDynamic Programming

##################################################################################################
# https://www.hackerrank.com/challenges/coin-change/problem
# The Coin Change Problem

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#


def getWays(needed_amount, couns_set):
    counter = [0] * (needed_amount + 1)
    for coin in couns_set:
        start = coin
        if start <= needed_amount:
            counter[start] += 1
            start += 1
        while start <= needed_amount:
            prev = start - coin
            counter[start] += counter[prev]
            start += 1
    return counter[-1]


def getWays_better(n, c):
    n_perms = [1]+[0]*n
    for coin in c:
        for i in range(coin, n+1):
            n_perms[i] += n_perms[i-coin]
    return n_perms[n]

# print(getWays(4, [1, 2, 3]))  # 4
# print(getWays(10, [2, 5, 3, 6]))  # 5

##################################################################################################
# https://www.hackerrank.com/challenges/hr-city/problem
# HackerRank City


def hackerrankCity(valueIn):
    result = 0
    n = len(valueIn)
    numArr = [1]
    pointArr = [0]
    res = [0]
    distance = 0  # Cross distance between furthest points
    for i in range(1, n + 1):
        a = valueIn[i - 1]
        num = numArr[i - 1]
        pointer = pointArr[i - 1]
        numArr.append((numArr[i - 1] * 4 + 2) % 1000000007)
        pointArr.append((pointer * 4 + (2 + 3 * num) * distance + a * (3 + 6 * num + 2 * num)) % 1000000007)
        res.append((res[i - 1] * 4 + pointer * (numArr[i] - num) * 4 + (
                    6 * num * 2 + 1) * a + num * num * 16 * a) % 1000000007)
        distance = (distance * 2 + 3 * a) % 1000000007
    # print(numArr)
    # print(pointArr)
    result = res[-1] % 1000000007
    return result


# print(hackerrankCity([2, 1]))

##################################################################################################
# https://www.hackerrank.com/challenges/maxsubarray/problem
# The Maximum Subarray


def maxSubarray(arr):
    # calculate max subsequence sum
    min_val = -10000
    sum_val = 0
    only_negative = True
    for val in arr:
        if val > 0:
            sum_val += val
            only_negative = False
        else:
            min_val = max(min_val, val)
    if only_negative:
        sum_val = min_val

    # maximum subarray sum
    result = 0
    cur_max = arr[0]
    prev_max = cur_max
    for i in range(1, len(arr)):
        val = arr[i]
        if cur_max < 0:
            cur_max = max(cur_max, val)
        elif val >= 0:
            cur_max += val
        else:
            prev_max = max(cur_max, prev_max)
            cur_max += val

    result = max(cur_max, prev_max)

    return [result, sum_val]

# print(maxSubarray([1, 2, 3, 4]))  # 10, 10
# print(maxSubarray([2, -1, 2, 3, 4, -5]))  # 10, 11
# print(maxSubarray([-2, -3, -1, -4, -6]))  # -1, -1
# print(maxSubarray([-1, 2, 3, -4, 5, 10]))  # 16, 20


def max_sum_subsequence(a, n):
    m = a[0]
    t = 0
    for i in range(n):
        m = max(m, a[i])
        if a[i] >= 0:
            t += a[i]
    return t if m >= 0 else m

def max_sum_subarray(a, n):
    f = a[0]
    ans = f
    for i in range(1, n):
        f = max(a[i], f + a[i])
        ans = max(ans, f)
    return ans

##################################################################################################
