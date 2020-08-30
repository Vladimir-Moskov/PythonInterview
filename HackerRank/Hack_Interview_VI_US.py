######################################################################
# https://www.hackerrank.com/contests/hack-the-interview-vi/challenges

######################################################################
# https://www.hackerrank.com/contests/hack-the-interview-vi/challenges/maximum-sum-10-1
# Array-Sum Operation

# 100% solution
def performOperations(N, op):
    result = [0] * len(op)
    ar = [i for i in range(1, N + 1)]
    key_set = set(ar)
    current_sum = sum(ar)
    for i, operation in enumerate(op):
        if operation in key_set:
            ar[0], ar[-1] = ar[-1], ar[0]
        else:
            key_set.remove(ar[-1])
            key_set.add(operation)
            current_sum = current_sum - ar[-1] + operation
            ar[-1] = operation

        result[i] = current_sum

    return result

N = 3
op = [4, 2]
# print(performOperations(N, op))

######################################################################
# https://www.hackerrank.com/contests/hack-the-interview-vi/challenges/constructing-a-tree
# Constructing a Tree locked

def result_to_tree_0(result):
    tree = [(1, 2)]
    root = 1
    next_root = 2
    for i in range(1, len(result)):
        if result[i] != result[i-1]:
            root = next_root
            next_root = i + 2
        tree.append((root, i + 2))
    return tree


def treeConstruction_0(N, X):
    # min tree size / edges sum
    if N > X:
        return [-1, -1]

    # max tree size / edges sum
    if sum([i for i in range(1, N )]) < X:
        return [-1, - 1]

    cur_val = N - 1
    result = [1] * (N - 1)
    for i in range(1, N):
        for j in range(N - 2, i, -1):
            if cur_val == X:
                return result_to_tree_0(result)
            cur_val += 1
            result[j] += 1

    return result_to_tree_0(result)

def result_to_tree(result):
    tree = []
    root = 1
    cur_root = 1
    k = 0
    for i in range(0, len(result)):
        if result[i] != result[i - 1]:
            cur_root = i + 1
        tree.append((cur_root, i + 2))
        k += 1
        if k == 2:
            cur_root -= 1
    return tree

def treeConstruction(N, X):

    # min tree size / edges sum
    if N > X:
        return [(-1, -1)]

    result = [i for i in range(1, N)]
    cur_val = sum(result)

    # max tree size / edges sum
    if cur_val < X:
        return [(-1, - 1)]

    i = 1
    j = len(result) - 1
    while cur_val > X:
        result[j] -= 1
        cur_val -= 1
        j -= 1
        if j == i - 1:
            i = i * 2
            j = len(result) - 1

    return result_to_tree(result)

# print(treeConstruction(5, 6))
# print(treeConstruction(5, 7))
# print(treeConstruction(3, 1))

# print(treeConstruction(6, 8))
# print(treeConstruction(5, 7))
# [1, 2, 3, 4, 5] # 15




# [1, 1, 1, 1, 1] # 5
# [1, 1, 1, 1, 2] # 6
# [1, 1, 1, 2, 2] # 7
# [1, 1, 2, 2, 2] # 8
# [1, 2, 2, 2, 2] # 9
# [1, 2, 2, 2, 3] # 10
# [1, 2, 2, 3, 3] # 11
# [1, 2, 3, 3, 3] # 12
# [1, 2, 3, 3, 4] # 13
# [1, 2, 3, 4, 4] # 14
# [1, 2, 3, 4, 5] # 15

######################################################################
# https://www.hackerrank.com/contests/hack-the-interview-vi/challenges/the-cup-game
# Solving for Queries with Cups

# slow solution -> 40% of score
def _countCups(n, balls, swaps, queries):
    result = []

    backets = [0] * (n + 1)

    for val in balls:
        backets[val] = 1

    for a, b in swaps:
        backets[a], backets[b] = backets[b], backets[a]

    for start, end in queries:
        result.append(sum(backets[start:(end + 1)]))

    return result

# faster solution -> 50% of score
def __countCups(n, balls, swaps, queries):
    result = []

    backets = set(balls)

    for a, b in swaps:
        if a in backets:
            if b not in backets:
                backets.remove(a)
                backets.add(b)
        else:
            if b in backets:
                backets.remove(b)
                backets.add(a)

    backets = sorted(list(backets))
    for start, end in queries:
        left_ind = 0
        right_ind = 0
        for i in range(len(backets)):
            if backets[i] > start:
                left_ind = i - 1
            elif backets[i] == start:
                left_ind = i

            if backets[i] > end:
                right_ind = i - 1
            elif backets[i] == end:
                right_ind = i
        result.append(right_ind - left_ind)

    return result

from bisect import bisect_left as bl, bisect_right as br

def countCups(n, balls, swaps, queries):
    # Write your code here
    m = set(balls)
    for i,j in swaps:
        if i in m and j not in m:
            m.add(j)
            m.remove(i)
        elif i not in m and j in m:
            m.remove(j)
            m.add(i)
    l = list(m)
    l.sort()
    return [br(l,j) - bl(l,i) for i,j in queries]

n = 4
m = 2
balls = [2, 4]
swaps = [[2, 4], [2, 1], [2, 3]]
queries = [[2, 4]]
# print(countCups(n, balls, swaps, queries)) # 2

n = 3
m = 1
balls = [2]
swaps = [[1, 2], [1, 3], [3, 1]]
queries = [[1, 2], [1, 3]]
# print(countCups(n, balls, swaps, queries)) # 1 1

n = 3
n = 100000
m = 2
balls = [1, 3]
swaps = [[1, 3], [3, 2]]
queries = [[1, 2], [3, 3]]
# print(countCups(n, balls, swaps, queries))

n = 4
m = 3
balls = [1, 3, 4]
swaps = [[3, 2], [1, 4]]
queries = [[1, 1], [2, 2], [3, 3], [4, 4]]
print(countCups(n, balls, swaps, queries))
######################################################################