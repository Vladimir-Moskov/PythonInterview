

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