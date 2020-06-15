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


print(hackerrankCity([2, 1]))

##################################################################################################