# https://www.hackerrank.com/challenges/grading/problem
# Grading Students


def gradingStudents(grades):
    # Write your code here
    for i, grade in enumerate(grades):
        if grade >= 38:
            rest = grade % 5
            grade += 5 - rest if rest > 2 else 0
            grades[i] = grade
    return grades

############################################################################################
# https://www.hackerrank.com/challenges/kangaroo/problem
# Kangaroo

def kangaroo(x1, v1, x2, v2):
    if x1 > x2 and v1 > v2:
        x1, x2, v1, v2 = x2, x1, v2, v1
    if x1 > x2 and v1 > v2:
        return "NO"
    if x2 > x1 and v2 > v1:
        return "NO"
    if v2 == v1:
        return "NO"
    if (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    return "NO"

############################################################################################
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# Divisible Sum Pairs

def divisibleSumPairs(n, k, ar):
    from collections import defaultdict
    import math
    result = 0
    dic_count = defaultdict(int)
    for i in ar:
        dic_count[i % k] += 1
    for i in range(int(k / 2) + 1):
        if i == 0 or i == k / 2:
            result += (dic_count[i] * (dic_count[i] - 1)) / 2
        else:
            result += dic_count[i] * dic_count[k-i]
    print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))
    return result

############################################################################################
# https://www.hackerrank.com/challenges/electronics-shop/problem
# Electronics Shop


def getMoneySpent(keyboards, drives, s, n, m):
    keyboards.sort(reverse=True)
    drives.sort()
    curr_max = -1
    init_j = 0

    for i in range(n):
        for j in range(init_j, m):
            if keyboards[i] + drives[j] > s:
                init_j = j
                break
            elif keyboards[i] + drives[j] > curr_max:
                curr_max = keyboards[i] + drives[j]

    return curr_max


def getMoneySpentNoSort(keyboards, drives, b):
    prices = [0] * b
    for keyboard in keyboards:
        if keyboard < b:
            prices[keyboard] = -1
    for drive in drives:
        if drive < b:
            if prices[drive] == 1:
                prices[drive] = 1
            else:
                prices[drive] = -2
    i = 1
    j = b - 1
    result = 0
    while i <= j:
        if (prices[i] == -1 or prices[i] == -2) and (prices[j] == 1 or prices[j] == -2):
            result = i + j
            break
        if (prices[i] == -1 or prices[i] == -2) and j >= b -i:
            j -= 1
        else:
            i += 1

    if b > result:
        j = result + 1
        i = b - j
        while i > 0:
            if (prices[i] == -1 or prices[i] == -2) and (prices[j] == 1 or prices[j] == -2):
                result = i + j
                break
            if (prices[i] == 1 or prices[i] == -2)  and j >= b -i:
                j += 1
            else:
                i -= 1
    return -1 if result == 0 else result

# print(getMoneySpent([3, 1], [3, 2, 8], 10))
# print(getMoneySpent([4], [5], 5))

############################################################################################
# https://www.hackerrank.com/challenges/bon-appetit/problem
# Bon Appétit


def bonAppetit(bill, k, b):
    dif = b - (sum(bill) - bill[k]) // 2
    if dif == 0:
        print("Bon Appetit")
    else:
        print(dif)


############################################################################################
# https://www.hackerrank.com/challenges/picking-numbers/problem
# Picking Numbers


def pickingNumbers(given_ar):
    given_ar.sort()
    result = 0
    i = 0
    j = 1
    while j < len(given_ar):
        if given_ar[j] - given_ar[i] < 2:
            j += 1
        else:
            result = max(result, j - i)
            i += 1
    result = max(result, j - i)

    print(pickingNumbers([4, 6, 5, 3, 3, 1]))  # 3
    return result

############################################################################################
# https://www.hackerrank.com/challenges/angry-professor/problem
# Angry Professor


def angryProfessor(k, arrival_times):
    for arrival_time in arrival_times:
        if arrival_time < 1:
            k -= 1
            if k == 0:
                return "NO"
    return "YES"

############################################################################################
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# Beautiful Days at the Movies


def beautifulDays(i, j, k):
    result = 0
    while i <= j:
        original = i
        reversed_num = 0
        num = original
        while num:
            rest = num % 10
            reversed_num = (reversed_num * 10) + rest
            num = num // 10
        print(reversed_num)
        if (original - reversed_num) % k == 0:
            result += 1
        i += 1

    return result

############################################################################################
# https://www.hackerrank.com/challenges/3d-surface-area/problem
# 3D Surface Area


def surfaceArea(A):
    # bottom + top sides
    result = len(A) * len(A[0]) * 2
    result += sum(A[0]) + sum(A[-1])
    result += sum(A[i][0] + A[i][-1] for i in range(len(A)))
    for i in range(len(A)):
        for j in range(len(A[0])):
            if j < len(A[0]) - 1:
                if A[i][j] > A[i][j + 1]:
                    result += A[i][j] - A[i][j + 1]
                else:
                    result += A[i][j + 1] - A[i][j]
            if i < len(A) - 1:
                if A[i][j] > A[i + 1][j]:
                    result += A[i][j] - A[i + 1][j]
                else:
                    result += A[i + 1][j] - A[i][j]

    return result

# A = [[1, 3, 4], [2, 2, 3], [1, 2, 4]]
# print(surfaceArea(A))
#
# some_list = [[1, 3, 4],
#              [2, 2, 3],
#              [1, 2, 4]]
# another_list = [[1, 3, 4], [2, 2, 3], [1, 2, 4]]
# print("Result: %s" % (some_list is list))

############################################################################################
# https://www.hackerrank.com/challenges/two-pluses/problem
# Ema's Supercomputer

GOOD = "G"
BAD = "B"

def twoPluses(grid):

def twoPluses(grid):
    result = 0
    width = len(grid[0])
    height = len(grid)
    result_matrix_left = [[0] * width for _ in range(height)]
    result_matrix_right = [[0] * width for _ in range(height)]
    result_matrix_top = [[0] * width for _ in range(height)]
    result_matrix_bottom = [[0] * width for _ in range(height)]

    for i in range(height):
        for j in range(width):
            if grid[i][j] == GOOD:
                if j == 0:
                    result_matrix_left[i][j] = 1
                else:
                    result_matrix_left[i][j] += 1 + result_matrix_left[i][j - 1]

                if i == 0:
                    result_matrix_top[i][j] = 1
                else:
                    result_matrix_top[i][j] += 1 + result_matrix_top[i - 1][j]
            else:
                result_matrix_left[i][j] = 0
                result_matrix_top[i][j] = 0

    for i in range(height - 1, -1, -1):
        for j in range(width - 1, -1, -1):
            if grid[i][j] == GOOD:
                if j == width - 1:
                    result_matrix_right[i][j] = 1
                else:
                    result_matrix_right[i][j] = 1 + result_matrix_right[i][j + 1]

                if i == height - 1:
                    result_matrix_bottom[i][j] = 1
                else:
                    result_matrix_bottom[i][j] = 1 + result_matrix_bottom[i + 1][j]
            else:
                result_matrix_right[i][j] = 0
                result_matrix_bottom[i][j] = 0
    prev_max = None
    prev_result = None
    for k in range(2):
        for i in range(height):
            for j in range(width):
                cur_min = min(result_matrix_left[i][j],  result_matrix_right[i][j],  result_matrix_top[i][j],  result_matrix_bottom[i][j])
                if result < cur_min:
                    result = cur_min
                    prev_max = (i, j)
        if k == 0:
            i, j = prev_max
            for n in range(result):
                result_matrix_left[i][j - n] = result_matrix_left[i][j + n] = result_matrix_left[i - n][j] = result_matrix_left[i + n][j] = 0
                result_matrix_right[i][j - n] = result_matrix_right[i][j + n] = result_matrix_right[i - n][j] = result_matrix_right[i + n][j] = 0
                result_matrix_top[i][j - n] = result_matrix_top[i][j + n] = result_matrix_top[i - n][j] = result_matrix_top[i + n][j] = 0
                result_matrix_bottom[i][j - n] = result_matrix_bottom[i][j + n] = result_matrix_bottom[i - n][j] = result_matrix_bottom[i + n][j] = 0
            n = j + result
            while n < len(result_matrix_left[i]) and result_matrix_left[i][n] > 0:
                result_matrix_left[i][n] = result_matrix_left[i][n - 1] + 1
                n += 1
            n = j - result
            while n >= 0 and result_matrix_right[i][n] > 0:
                result_matrix_right[i][n] = result_matrix_right[i][n + 1] + 1
                n -= 1
            n = i - result
            while n >= 0 and result_matrix_bottom[n][j] > 0:
                result_matrix_bottom[n][j] = result_matrix_bottom[n + 1][j] + 1
                n -= 1
            n = i + result
            while n < len(result_matrix_top) and result_matrix_top[n][j] > 0:
                result_matrix_top[n][j] = result_matrix_top[n - 1][j] + 1
                n += 1
            prev_result = result
            result = 0

    return ((result - 1) * 4 + 1) * ((prev_result - 1) * 4 + 1)

grid = ['GGGGGG', 'GBBBGB', 'GGGGGG', 'GGBBGB', 'GGGGGG']  # 5
# print(twoPluses(grid))
grid = ['BGBBGB', 'GGGGGG', 'BGBBGB', 'GGGGGG', 'BGBBGB', 'BGBBGB']  # 25
# print(twoPluses(grid))
grid = ["GBGBGGB",
        "GBGBGGB",
        "GBGBGGB",
        "GGGGGGG",
        "GGGGGGG",
        "GBGBGGB",
        "GBGBGGB"]

print(twoPluses(grid))  # 45
