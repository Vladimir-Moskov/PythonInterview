######################################################################################
# https://www.hackerrank.com/challenges/an-interesting-game-1/problem
# Gaming Array


# O(n^2) solution
def gamingArray_naive(arr):
    result = 0
    end = len(arr) - 1
    while end >= 0:
        i = 0
        max_i = 0
        while i <= end:
            if arr[max_i] < arr[i]:
                max_i = i
            i += 1
        result += 1
        end = max_i - 1

    if result % 2 == 0:
        return "ANDY"
    return "BOB"


# O(n) solution
def gamingArray(arr):
    result = 1
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
            result += 1

    if result % 2 == 0:
        return "ANDY"
    return "BOB"

arr = [2, 3, 5, 4, 1]  # bob
#print(gamingArray(arr))
arr = [5, 2, 6, 3, 4]  # andy
#print(gamingArray(arr))

######################################################################################
# https://www.hackerrank.com/challenges/flipping-the-matrix/problem
# Flipping the Matrix


def flippingMatrix(matrix):
    result = 0
    n = len(matrix) // 2

    for i in range(n):
        for j in range(n):
            ar = [matrix[i][j], matrix[i][-(1 + j)], matrix[-(1 + i)][j], matrix[-(1 + i)][-(1 + j)]]
            val = max(ar)
            result += val
    return result

case_1 = [[1, 2],
          [3, 4]]
#print(flippingMatrix(case_1)) # 4


case_2 = [[112, 42, 83, 119],
          [56, 125, 56, 49],
          [15, 78, 101, 43],
          [62, 98, 114, 108]]
# print(flippingMatrix(case_2)) # 414



######################################################################################
# https://www.hackerrank.com/challenges/construct-the-array/problem
# Construct the Array


def countArray(n, k, x):
    result = 1 if x != 1 else 0
    next_res = k - 1
    mod = 1000000007
    for _ in range(n - 2):
        result = (next_res - result) % mod
        next_res = (next_res * (k - 1)) % mod

    return result


# print(countArray(761, 99, 1,)) # 236568308

######################################################################################
# https://www.hackerrank.com/challenges/red-john-is-back/problem
# Red John is Back


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def redJohn(n):
    pre_calc = [0] * n
    result = 0
    if n < 4:
        return 0
    pre_calc[0] = 1
    pre_calc[1] = 1
    pre_calc[2] = 1
    pre_calc[3] = 2

    for i in range(4, n):
        sum_4 = pre_calc[i - 4] + pre_calc[i - 1]
        pre_calc[i] = sum_4

    for i in range(2, pre_calc[-1] + 1):
        if isPrime(i):
            result += 1
    return result


# print(redJohn(1))  # 1 -> 0
# print(redJohn(5))  # 3 -> 2
# print(redJohn(7))  # 5 -> 3
# print(redJohn(8))  # 5 -> 4

######################################################################################



