# Hack the Interview IV (U.S.)
# 45 / 1217 participants

#################################################################################################
# https://www.hackerrank.com/contests/hack-the-interview-iv/challenges/good-binary-string
# Valid Binary String

# 100% -> 10/10 points
# O(n) solution
def minimumMoves(s, d):
    result = 0
    start = 0
    counter = 0
    while start < len(s):
        if s[start] == "0":
            counter += 1
            if counter == d:
                result += 1
                counter = 0
        else:
            counter = 0
        start += 1

    return result

s = "00100" # 2
d = 2
s = "101" # 0
d = 2
# print(minimumMoves(s, d))  # 2

#################################################################################################
# https://www.hackerrank.com/contests/hack-the-interview-iv/challenges/arrange-students
# Arrange Students

# Score: 20 / 20
# O(n) solution
def arrangeStudents(a, b):
    a.sort()
    b.sort()
    a_i = 0
    b_i = 0
    is_a = 0  # 0 - does not matter, -1 is for b, 1 is for a
    for i in range(len(a) * 2 - 1):
        if a_i == len(a):
            if is_a == -1:
                return "NO"
            else:
                break
        elif b_i == len(a):
            if is_a == 1:
                return "NO"
            else:
                break
        if a[a_i] < b[b_i]:
            a_i += 1
            if is_a == 1:
                return "NO"
            else:
                is_a = 1
        elif a[a_i] == b[b_i]:
                is_a = 0
                b_i += 1
                a_i += 1
        else:
            b_i += 1
            if is_a == -1:
                return "NO"
            else:
                is_a = -1
    return "YES"
#
# a = [1, 3]
# b = [2, 4]
# print(arrangeStudents(a, b))  # Yes
# #
# a = [1, 2]
# b = [3, 4]
# print(arrangeStudents(a, b))  # No
#
# a = [2, 3, 5]
# b = [1, 3, 4]
# print(arrangeStudents(a, b))  # Yes
# #
# a = [1, 2, 5]
# b = [1, 3, 5]
# print(arrangeStudents(a, b))  # Yes

#################################################################################################
# https://www.hackerrank.com/contests/hack-the-interview-iv/challenges/optimal-path-1
# Optimal Network Routing

# Score: 300 / 30 !!!!!

from collections import deque

def getMinEffort(C):

    visited = [[0] * len(C[0]) for _ in range(len(C))]
    start = (0, 0)
    visited[0][0] = 1
    min_val = 0
    path_q = deque([start])
    touched_q = {}
    while path_q:
        row, col = path_q.popleft()
        if row == len(C) - 1 and col == len(C[0]) - 1:
            break
        next_row = row - 1
        if 0 <= next_row < len(C) and visited[next_row][col] != 1:
            dif = C[row][col] - C[next_row][col]
            dif = -dif if dif < 0 else dif
            p = (next_row, col)
            if dif <= min_val:
                path_q.append(p)
                visited[next_row][col] = 1
                if p in touched_q:
                    del touched_q[p]
            else:
                if p not in touched_q or touched_q[p][0] > dif:
                    touched_q[p] = (dif, next_row, col)


        next_row = row + 1
        if 0 <= next_row < len(C) and visited[next_row][col] != 1:
            dif = C[row][col] - C[next_row][col]
            dif = -dif if dif < 0 else dif
            p = (next_row, col)
            if dif <= min_val:
                path_q.append(p)
                visited[next_row][col] = 1
                if p in touched_q:
                    del touched_q[p]
            else:
                # touched_q.append((dif, next_row, col))
                if p not in touched_q or touched_q[p][0] > dif:
                    touched_q[p] = (dif, next_row, col)

        next_col = col - 1
        if 0 <= next_col < len(C[0]) and visited[row][next_col] != 1:
            dif = C[row][col] - C[row][next_col]
            dif = -dif if dif < 0 else dif
            p = (row, next_col)
            if dif <= min_val:
                path_q.append(p)
                visited[row][next_col] = 1
                if p in touched_q:
                    del touched_q[p]
            else:
                if p not in touched_q or touched_q[p][0] > dif:
                    touched_q[p] = (dif, row, next_col)

        next_col = col + 1
        if 0 <= next_col < len(C[0]) and visited[row][next_col] != 1:
            dif = C[row][col] - C[row][next_col]
            dif = -dif if dif < 0 else dif
            p = (row, next_col)
            if dif <= min_val:
                path_q.append(p)
                visited[row][next_col] = 1
                if p in touched_q:
                    del touched_q[p]
            else:
                if p not in touched_q or touched_q[p][0] > dif:
                    touched_q[p] = (dif, row, next_col)

        if not path_q and touched_q:
            cur_min = 100000000

            next_items = []
            for item in touched_q.values():
                dif, row_val, col_val = item
                if cur_min > dif:
                    next_items = [item]
                    cur_min = dif
                elif cur_min == dif:
                    next_items.append(item)

            for dif, row_val, col_val in next_items:
                p = (row_val, col_val)
                path_q.append(p)
                visited[row_val][col_val] = 1
                del touched_q[p]

            if path_q:
                min_val = cur_min

    return min_val

# 6
# C = [
#     [12, 6, 5, 3],
#     [6, 13, 3, 15],
#     [8, 2, 6, 9]
# ]
# print(getMinEffort(C))
# # 4
# C =  [
#     [5, 1, 3, 2],
#     [7, 4, 1, 8],
#     [6, 7, 5, 9]
# ]
# print(getMinEffort(C))
# # 5
# C =  [
#     [13, 14, 13, 1],
#     [8, 12, 12, 9],
#     [15, 15, 14, 14 ],
#     [15, 10, 10, 5]
# ]
# print(getMinEffort(C))

#################################################################################################
# https://www.hackerrank.com/contests/hack-the-interview-iv/challenges/maximum-or-1
# Number of integers

def getNumberOf(max_val, K):
    result = 0
    min_k = 10 ** (K - 1)
    if min_k + 1 > max_val:
        return 0

    incriment = 9 ** K

    next_k = min_k * 10
    while next_k <= max_val:
        next_k *= 10

    dif = max_val - next_k // 10
    if dif > 0:
        temp = int(max_val / next_k * 10) - 1
        if K - 1 < 0:
            result += getNumberOf(0, K - 1)
    return result

def getNumberOfIntegers(L, R, K):
    L = int(L)
    R = int(R)
    result = getNumberOf(R, K) - getNumberOf(L, K)

    return result

# brute force

def getNumberOfIntegers(L, R, K):
    result = 0
    L = int(L)
    R = int(R)
    for i in range(L + 1, R + 1):
        tmp = str(i)
        if tmp.count("0") == len(tmp) - K:
            result += 1
    return result

# print(getNumberOfIntegers(1, 100, 1)) # 18
# print(getNumberOfIntegers(10, 55, 2)) # 4
# print(getNumberOf(1, 1))
# print(getNumberOf(10, 1))
# print(getNumberOf(100, 1)) # 18
# print(getNumberOf(255, 1)) # 19

# print(getNumberOf(1, 2)) # 0
# print(getNumberOf(10, 2)) # 0
# print(getNumberOf(100, 2)) # 81
#print(getNumberOf(101, 2)) # 82

#################################################################################################

dp = []
M = 102
K = 0

def countInRangeUtil(pos, cnt, tight, num):
    # Last position
    if pos == len(num):

        # If count of non zero digits
        # is less than or equal to K
        if cnt == K:
            return 1
        return 0

    # If this result is already computed
    # simply return it
    if dp[pos][cnt][tight] != -1:
        return dp[pos][cnt][tight]

    ans = 0

    # Maximum limit upto which we can place
    # digit. If tight is 1, means number has
    # already become smaller so we can place
    # any digit, otherwise num[pos]
    limit = 9 if tight else num[pos]

    for dig in range(limit + 1):
        currCnt = cnt

        # If the current digit is nonzero
        # increment currCnt
        if dig != 0:
            currCnt += 1

        currTight = tight

        # At this position, number becomes
        # smaller
        if dig < num[pos]:
            currTight = 1

        # Next recursive call
        ans += countInRangeUtil(pos + 1, currCnt, currTight, num)

    dp[pos][cnt][tight] = ans
    return dp[pos][cnt][tight]

def countInRange(x):
    global dp, K, M

    num = []
    while x:
        num.append(x % 10)
        x //= 10

    num.reverse()

    # Initialize dp
    dp = [[[-1, -1] for i in range(M)] for j in range(M)]
    return countInRangeUtil(0, 0, 0, num)


def getNumberOfIntegers_2(L, R, K_):
    global dp, K, M
    dp = []
    M = 100
    L = int(L)
    R = int(R)
    K = K_

    result = countInRange(R) - countInRange(L)

    return result
# print(getNumberOfIntegers_2(1, 100, 1)) # 18
# print(getNumberOfIntegers_2(1, 1000, 1)) # 27
# print(getNumberOfIntegers_2(1, 10000, 1)) # 36
# print(getNumberOfIntegers_2(1, 100000, 1)) # 45
#
# print(getNumberOfIntegers_2(1, 300, 2)) # 81
# print(getNumberOfIntegers_2(1, 3000, 2)) # 243
# print(getNumberOfIntegers_2(1, 30000, 2)) # 486
# print(getNumberOfIntegers_2(1, 300000, 2)) # 810
#
# print(getNumberOfIntegers_2(1, 100, 3)) # 0
# print(getNumberOfIntegers_2(1, 1000, 3)) # 729
# print(getNumberOfIntegers_2(1, 10000, 3)) # 2916
# print(getNumberOfIntegers_2(1, 100000, 3)) # 7290
#
# print(getNumberOfIntegers_2(10, 55, 2)) # 41
# print(getNumberOfIntegers_2(1, 100, 1)) # 18
# print(getNumberOfIntegers_2(1, 100, 2)) # 81

# score 40 / 40 !!!!!!!!!!!!!!!!!!
def k_nonzero_numbers(R, n, K):

    dp = [[[0] * (K + 2) for _ in range(2)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        sm = 0
        while sm < 2:
            for j in range(K + 1):
            # for j in range(K):
                x = 0
                while x <= (9 if sm > 0 else int(R[i])):
                    ind_1 = 0
                    if sm > 0 or x < int(R[i]):
                        ind_1 = 1
                    ind_2 = j + (x > 0)
                    dp[i + 1][ind_1][ind_2] += dp[i][sm][j]
                    x += 1
            sm += 1
    return dp[n][0][K] + dp[n][1][K]

def getNumberOfIntegers_3(L_str, R_str, K):
    L = int(L_str)
    R = int(R_str)

    result = k_nonzero_numbers(R_str, len(R_str), K) - k_nonzero_numbers(L_str, len(L_str), K)

    return result % (1000000000 + 7)

print(getNumberOfIntegers_3("10", "55", 2))  # 41
print(getNumberOfIntegers_3("1", "100", 1))  # 18
print(getNumberOfIntegers_3("1", "100", 2)) # 81