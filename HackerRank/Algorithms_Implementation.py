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
