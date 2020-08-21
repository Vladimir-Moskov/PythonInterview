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

print(treeConstruction(5, 6))
print(treeConstruction(5, 7))
print(treeConstruction(3, 1))

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


