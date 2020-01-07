

# Complete the climbingLeaderboard function below.
def climbingLeaderboard_0(scores, alice):
    result = []
    rank = [1]
    for i in range(1, len(scores)):
        if scores[i-1] == scores[i]:
            rank.append(rank[i-1])
        else:
            rank.append(rank[i-1] + 1)

    k = len(scores) - 1
    for i in alice:
        while i > scores[k]:
            k -= 1
            if k < 0:
                result.append(1)
                break
        if k >= 0:
            if i == scores[k]:
                result.append(rank[k])
            else:
                result.append(rank[k] + 1)

    return result

def climbingLeaderboard(scores, alice):
    scores_set = sorted(list(set(scores)), reverse=True)
    result = []
    k = len(scores_set) - 1
    for i in alice:
        while i > scores_set[k]:
            k -= 1
            if k < 0:
                result.append(1)
                break
        if k >= 0:
            if i == scores_set[k]:
                result.append(k + 1)
            else:
                result.append(k + 2)

    return result

scores = [100,100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]

print(climbingLeaderboard(scores, alice))

scores = [100, 90, 90, 80, 75, 60]
alice = [50, 65, 77, 90, 102]

print(climbingLeaderboard(scores, alice))

import math
import os
import random
import re
import sys

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     scores_count = int(input())
#
#     scores = list(map(int, input().rstrip().split()))
#
#     alice_count = int(input())
#
#     alice = list(map(int, input().rstrip().split()))
#
#     result = climbingLeaderboard(scores, alice)
#
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()

# https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings
def commonChild(given_str_1, given_str_2):
    size = len(given_str_1)
    matrix_str = [[0 for i in range(size)] for j in range(size)]

    # create matrex
    for i, char_i in enumerate(given_str_2):
        for j, char_j in enumerate(given_str_1):
            matrix_str[i][j] = int(char_i == char_j)

    # process matrix
    for i, line in enumerate(matrix_str):
        for j, flag in enumerate(matrix_str):
            if i != 0 and j != 0:
                new_val = matrix_str[i][j] + max(matrix_str[i-1][j-1], matrix_str[i][j-1])
                matrix_str[i][j] = max(new_val, matrix_str[i-1][j])

    result = matrix_str[i][j]
    return result

# s1 = "HARRY"
# s2 = "SALLY" # 2
s1 = "SHINCHAN"
s2 = "NOHARAAA" # 3
# s1 = "OUDFRMYMAW"
# s1 = "AWHYFCCMQX" # 2
print(commonChild(s1, s2))


# Left Rotation
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def rotLeft(given_ar, shift_size):
    shift_size = shift_size % len(given_ar)
    if shift_size == 0:
        return given_ar

    result_ar = given_ar[shift_size:] + given_ar[:shift_size]
    return result_ar

ar = [1, 2, 3, 4, 5]
val = 4
print(rotLeft(ar, val))
