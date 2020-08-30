
# Hack the Interview III
# https://www.hackerrank.com/contests/hacktheinterview3/challenges

#########################################################################################
# https://www.hackerrank.com/contests/hacktheinterview3/challenges/distribution-in-m-bins
# Product Distribution

def maxScore(a, m):
    result = 0
    if m >= len(a):
        return sum(a) % 1000000007
    a.sort()
    k = 1
    j = 0
    for i, val in enumerate(a):
        if i + m <= len(a):
            if j == m:
                j = 0
                k += 1
            j += 1
        result = (result + k * val) % 1000000007

    return result




# case 0 - 27
a = [1, 5, 4, 2, 3]
m = 2
# print(maxScore(a, m))

# case 1 - 21
a = [4, 1, 9, 7]
m = 4
# print(maxScore(a, m))

#########################################################################################
# https://www.hackerrank.com/contests/hacktheinterview3/challenges/maximal-char-requests
# Maximal Char Requests

# slower - solution 50% of score
def _getMaxCharCount_1(s, queries):
    result = []
    s = list(s.lower())
    for start, end in queries:
        t_str = s[start:(end + 1)]
        max_ch = max(t_str)
        result.append(t_str.count(max_ch))

    return result

# faster - solution 50% of score
def _getMaxCharCount_2(s, queries):
    result = []
    s = s.lower()
    matrix = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        cur_max = s[i]
        cur_max_count = 1
        matrix[i][i] = cur_max_count
        for j in range(i + 1, len(s)):
            if cur_max == s[j]:
                cur_max_count += 1
            else:
                cur_max = max(cur_max, s[j])
                if cur_max == s[j]:
                    cur_max_count = 1

            matrix[i][j] = cur_max_count

    for start, end in queries:
        result.append(matrix[start][end])

    return result

def getMaxCharCount(s, queries):
    first_ch = 97
    result = []
    s = s.lower()
    s = list(map(ord, s))
    matrix = [[0] * 26 for _ in range(len(s) + 1)]

    for i in range(1, len(s) + 1):
        val = s[i - 1] - first_ch
        matrix[i][val] = 1
        for j in range(26):
            matrix[i][j] += matrix[i - 1][j]

    for start, end in queries:
        dif_ar = [matrix[end + 1][i] - matrix[start][i] for i in range(26)]
        for i in range(25, -1, -1):
            if dif_ar[i] != 0:
                result.append(dif_ar[i])
                break

    return result

s = "ddaaa"
queries = [[0, 4]]
# print(getMaxCharCount(s, queries)) # 2

s = "aAabBcba"
queries = [[2, 6],
            [1, 2],
            [2, 2],
            [0, 4],
            [0, 7]]

# queries = [[0, 0], [7, 7]]

s = "qqabcdefghijklmnopqrstuvwxyzggg"
queries = [
    [0, 0],
    [30, 30]
    ]
# print(getMaxCharCount(s, queries)) # 1 2 1 2 1

#########################################################################################
# https://www.hackerrank.com/contests/hacktheinterview3/challenges/yashs-party
# Configuring Project Management

from collections import deque, defaultdict

def _configureProjectPresentation(n, friendships):
    result = [-1]
    edges = [set() for i in range(n + 1)]


    for x, y in friendships:
        edges[x].add(y)
        edges[y].add(x)

    visited = set([2, 1])
    current_friend_2 = set(edges[2])
    q = deque(edges[2])
    current_friend_2.add(2)

    while q:
        next_q = set()
        for val in q:
            if val not in visited:
                visited.add(val)
                current_friend_2.add(val)
                next_q.update(edges[val])

        q = deque(next_q)

    q = deque(edges[1])
    current_friend = set()
    for val in edges[1]:
        if val not in current_friend_2:
            current_friend.add(val)
    # current_friend = set(edges[1])
    # if 2 in current_friend:
    #     current_friend.remove(2)
    # visited = set([2, 1])
    #
    # while q:
    #     next_q = set()
    #     for val in q:
    #         if val not in visited:
    #             visited.add(val)
    #             if val not in current_friend_2:
    #                 current_friend.add(val)
    #                 next_q.update(edges[val])
    #             else:
    #                 if val in current_friend:
    #                     current_friend.remove(val)
    #
    #     q = deque(next_q)
    if current_friend:
        result = list(current_friend)
        result.sort()

    return result

from collections import defaultdict


def configureProjectPresentation(n, friendships):
    g = defaultdict(list)

    for a, b in friendships:
        g[a].append(b)
        g[b].append(a)

    invited = []
    uninvited = [2]
    invited.extend(g[1])
    invited = set(invited)

    for i in g[2]:
        if i == 1:
            continue
        uninvited.append(i)
        uninvited.extend(g[i])
    uninvited = set(uninvited)
    result = set()
    for i in invited:
        if i not in uninvited and i != 1:
            result.add(i)

    if result:
        result = sorted(result)
    else:
        result = [-1]

    return result


n = 3
friendships = [
    [1, 2],
    [3, 2]]
# print(configureProjectPresentation(n, friendships))

n = 9
friendships = [[1, 3],
[1, 4],
[3, 2],
[5, 6],
[7, 1],
[2, 8],
[8, 9],
[9, 1]]
# print(configureProjectPresentation(n, friendships))

n = 2
friendships = [[1, 2]]
# print(configureProjectPresentation(n, friendships))

#########################################################################################
# https://www.hackerrank.com/contests/hacktheinterview3/challenges/flipped-beauty
# Minimum String Co-Efficient


def minStringCoeff(s, p):
    result = 0

    return result