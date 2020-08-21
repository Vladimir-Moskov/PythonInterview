##############################################
# https://www.hackerrank.com/challenges/jim-and-the-skyscrapers/problem
# Jim and the Skyscrapers

# O(n^2)
def _solve(arr):
    result = 0
    top_dic = {}
    for i, val in enumerate(arr):
        if val not in top_dic:
            top_dic[val] = []
            k = 1
            for j in range(i + 1, len(arr)):
                if arr[j] == val:
                    k += 1
                elif arr[j] > val:
                    top_dic[val].append(k)
                    k = 0
            top_dic[val].append(k)
    for top in top_dic.values():
        for val in top:
            if val > 1:
                result += (val - 1) * val

    return result

from collections import deque

# O(n)
def solve(arr):
    result = 0
    stack_val = deque()
    stack_count = {}

    for i, val in enumerate(arr):
        if len(stack_val):
            if val == stack_val[-1]:
                stack_count[val] += 1
            elif val < stack_val[-1]:
                stack_count[val] = 1
                stack_val.append(val)
            else:
                while stack_val and val > stack_val[-1]:
                    prev = stack_val.pop()
                    if stack_count[prev] > 1:
                        result += (prev - 1) * prev
                    stack_count[prev] = 0
                if not stack_val or val < stack_val[-1]:
                    stack_val.append(val)
                    stack_count[val] = 1
                else:
                    stack_count[val] += 1
        else:
            stack_val.append(val)
            stack_count[val] = 1

    for prev in stack_count.values():
        result += (prev - 1) * prev

    return result

arr = [3, 2, 1, 2, 3, 3]
print(solve(arr)) # 8

arr = [1, 1000, 1]
print(solve(arr)) # 0
# 12 -> 12 21
# 123 -> 12 13 21 23 31 32
# 1234 -> 12 13 14 21 23 24 31 32 34 41 42 43
# 12345 -> 12 13 14 15 21 23 24 25 31 32 34 35 41 42 43 45 51 52 53 54
##############################################
