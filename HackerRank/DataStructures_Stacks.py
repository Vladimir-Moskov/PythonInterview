#############################################################################
# https://www.hackerrank.com/challenges/equal-stacks/problem
# Equal Stacks

def equalStacks(h1, h2, h3):
    sum_1 = sum(h1)
    sum_2 = sum(h2)
    sum_3 = sum(h3)
    last_1 = 0
    last_2 = 0
    last_3 = 0

    while not (sum_1 == sum_2 and sum_1 == sum_3):
        if sum_1 >= sum_2 and sum_1 >= sum_3:
            sum_1 -= h1[last_1]
            last_1 += 1
        elif sum_2 >= sum_1 and sum_2 >= sum_3:
            sum_2 -= h2[last_2]
            last_2 += 1
        elif sum_3 >= sum_1 and sum_3 >= sum_1:
            sum_3 -= h3[last_3]
            last_3 += 1

    return sum_1

h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]

h1 = [1, 1, 1, 1, 2]
h2 = [3, 7]
h3 = [1, 3, 1]

# print(equalStacks(h1, h2, h3))

#############################################################################
# https://www.hackerrank.com/challenges/maximum-element/problem
# Maximum Element

#!/bin/python3


import os
from collections import deque

#
def naximumElement(n, queries):
    stack_deque = deque()
    max_stack = deque()
    curr_max = 0
    result = []
    for q in queries:
        if q[0] == 1:
            stack_deque.append(q[1])
            curr_max = max(curr_max, q[1])
            max_stack.append(curr_max)
        elif q[0] == 2:
            stack_deque.pop()
            max_stack.pop()
            if max_stack:
                curr_max = max_stack[-1]
            else:
                curr_max = 0
        else:
            result.append(curr_max)
    return result


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     queries = []
#
#     for _ in range(n):
#         queries.append(list(map(int, input().rstrip().split())))
#
#     result = naximumElement(n, queries)
#
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()

queries = [
    [1, 97],
    [2],
    [1, 20],
    [2],
    [1, 26],
    [1, 20],
    [2],
    [3],
    [1, 91],
    [3]
]

# print(naximumElement(n, queries))

#############################################################################