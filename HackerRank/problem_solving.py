# TODO - clean up here!!!

##############################################
# Maximum Subarray Sum
from bisect import insort, bisect_right


def maximumSum(a, m):
    # Create prefix tree
    prefix = [0] * len(a)
    curr = 0;
    for i in range(len(a)):
        curr = (a[i] % m + curr) % m
        prefix[i] = curr

    # Compute max modsum
    pq = [prefix[0]]
    maxmodsum = max(prefix)
    for i in range(1, len(a)):
        # Find cheapest prefix larger than prefix[i]
        left = bisect_right(pq, prefix[i])
        if left != len(pq):
            # Update maxmodsum if possible
            modsum = (prefix[i] - pq[left] + m) % m
            maxmodsum = max(maxmodsum, modsum)

        # add current prefix to heap
        insort(pq, prefix[i])

    return maxmodsum


def maximumSum2(a, m):
    ar_len = len(a)
    result_set = set()
    for i in range(ar_len):
        cur_val = 0
        for j in range(i, ar_len):
            cur_val += a[j]
            result_set.add(cur_val % m)
    result = max(result_set)
    return result


#############################################
# Complete the climbingLeaderboard function below.
def climbingLeaderboard_0(scores, alice):
    result = []
    rank = [1]
    for i in range(1, len(scores)):
        if scores[i - 1] == scores[i]:
            rank.append(rank[i - 1])
        else:
            rank.append(rank[i - 1] + 1)

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


scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]

# print(climbingLeaderboard(scores, alice))

scores = [100, 90, 90, 80, 75, 60]
alice = [50, 65, 77, 90, 102]

# print(climbingLeaderboard(scores, alice))

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
                new_val = matrix_str[i][j] + max(matrix_str[i - 1][j - 1], matrix_str[i][j - 1])
                matrix_str[i][j] = max(new_val, matrix_str[i - 1][j])

    result = matrix_str[i][j]
    return result


# s1 = "HARRY"
# s2 = "SALLY" # 2
s1 = "SHINCHAN"
s2 = "NOHARAAA"  # 3


# s1 = "OUDFRMYMAW"
# s1 = "AWHYFCCMQX" # 2
# print(commonChild(s1, s2))


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


# print(rotLeft(ar, val))


# =================
def minimumBribes(given_q):
    result = 0
    # bribe_dic = {}
    for index, val in enumerate(given_q):
        # dif = val - 1 - index
        dif = 0
        for j in range(index + 1, len(given_q)):
            dif += int(given_q[j] < val)
        if dif > 2:
            result = -1
            break
        elif dif > 0:
            result += dif

    return "Too chaotic" if result == -1 else result


def minimumBribes_optimal(q):
    bribes = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            return 'Too chaotic'
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    return "Too chaotic" if bribes == -1 else bribes


"Too chaotic"
case_1 = [2, 1, 5, 3, 4]  # 3
case_2 = [2, 5, 1, 3, 4]  # ---
case_3 = [1, 2, 5, 3, 7, 8, 6, 4]  # 7


# print(minimumBribes(case_1))
# print(minimumBribes(case_2))
# print(minimumBribes(case_3))

############################################################


def minimumSwaps_BrutForce(given_ar):
    result = 0
    if len(given_ar) < 2:
        return 0
    start_index = 0
    while start_index < len(given_ar) - 1:
        cur_elem = given_ar[start_index]
        if cur_elem != start_index:
            next_index = start_index
            next_min = given_ar[next_index]
            next_min_index = next_index
            while next_index < len(given_ar):
                next_elem = given_ar[next_index]
                if cur_elem > next_elem:
                    if next_elem < next_min:
                        next_min = next_elem
                        next_min_index = next_index
                next_index += 1
            # do swap
            if next_min_index != start_index:
                given_ar[start_index], given_ar[next_min_index] = given_ar[next_min_index], given_ar[start_index]
                result += 1
            else:
                start_index += 1
    return result


def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i + 1:
            swaps += 1
            t = arr[i]
            arr[i] = i + 1
            arr[temp[i + 1]] = t
            temp[t] = temp[i + 1]
    return swaps


case_1 = [4, 3, 1, 2]  # 3
case_2 = [2, 3, 4, 1, 5]  # 3
case_3 = [1, 3, 5, 2, 4, 6, 7]  # 3


# print(minimumSwaps(case_1))
# print(minimumSwaps(case_2))
# print(minimumSwaps(case_3))

#########################################################################

def maxSubsetSum(arr):
    result = arr[0]
    if len(arr) < 3:
        return result
    matrix_sum = [[0 for i in range(len(arr) - 2)] for j in range(len(arr) - 2)]

    for i in range(len(arr) - 2):
        line = matrix_sum[i]
        for j in range(0, i + 1):
            el_x = arr[j]  # if i - j < 2 else max(arr[j], matrix_sum[i - 2][j])
            el_y = arr[i + 2]
            new_sum = el_x + el_y
            matrix_sum[i][j] = max(new_sum, el_y)
            result = max(result, new_sum)
    return result


def maxSubsetSum0(arr):
    dp = []
    dp.append(arr[0])
    dp.append(max(arr[:2]))
    ans = max(dp)
    for a in arr[2:]:
        dp.append(max(max(dp[-2] + a, a), ans))
        ans = max(ans, dp[-1])
    return ans


case_1 = [3, 7, 4, 6, 5]  # 13
case_2 = [2, 1, 5, 8, 4]  # 11
case_3 = [3, 5, -7, 8, 10]  # 15


# print(maxSubsetSum(case_1))
# print(maxSubsetSum(case_2))
# print(maxSubsetSum(case_3))


######################
# https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming&h_r=next-challenge&h_v=zen

def abbreviation(str_val, str_abr):
    calculation_line = [0 for _ in str_val]
    if len(str_val) >= len(str_abr):
        for capital_abr in str_abr:
            has_letter = False
            for i, not_cap_str in enumerate(str_val):
                has_letter = has_letter or not_cap_str.upper() == capital_abr
                cur_fit = not_cap_str.islower() or not_cap_str.upper() == capital_abr
                cur_fit = calculation_line[i] == 1 or cur_fit
                calculation_line[i] = int(cur_fit)
                if not cur_fit:
                    break
            if not has_letter:
                calculation_line[-1] = 0
                break
    result = calculation_line[-1] == 1
    return "YES" if result else "NO"


def abbreviation_0(a, b):
    m, n = len(a), len(b)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n + 1):
        for j in range(1, m + 1):
            if a[j - 1] == b[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif a[j - 1].upper() == b[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1]
            elif a[j - 1].islower():
                dp[i][j] = dp[i][j - 1]
    return "YES" if dp[n][m] else "NO"


case_1_0 = "daBcd"  # Y
case_1_1 = 'ABC'
case_2_0 = "AbCdE"  # N
case_2_1 = 'AFE'
case_3_0 = "AfPZN"  # N
case_3_1 = 'APZNC'

# print(abbreviation(case_1_0, case_1_1))
# print(abbreviation(case_2_0, case_2_1))
# print(abbreviation(case_3_0, case_3_1))
###################

# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem

from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"Player: name = {self.name}, score = {self.score}"

    def comparator(a, b):
        if a.score == b.score:
            if a.name == b.name:
                return 0
            elif a.name < b.name:
                return - 1
            else:
                return 1
        else:
            if a.score > b.score:
                return - 1
            else:
                return 1


data = [Player('amy', 100), Player('david', 100), Player('heraldo', 50), Player('aakansha', 75), Player('aleksa', 150)]
data = sorted(data, key=cmp_to_key(Player.comparator))


# print(data)

################
# https://www.hackerrank.com/challenges/fraudulent-activity-notifications

def activityNotifications(expenditure, days):
    result = 0
    if len(expenditure) < days:
        return result

    midl_index = int(days // 2)
    sub_ar = expenditure[:days]
    sub_ar.sort()
    if days % 2 == 0:
        midl_index_start = midl_index - 1
        midl_index_end = midl_index
    else:
        midl_index_start = midl_index
        midl_index_end = midl_index

    for i in range(days, len(expenditure) - 1):
        median = sub_ar[midl_index_start] + sub_ar[midl_index_end]
        if median <= expenditure[i]:
            result += 1
        # sub_ar.append(expenditure[i])
        sub_ar.remove(sub_ar[0])
        for k, el in enumerate(sub_ar):
            if expenditure[i] < sub_ar[k]:
                break
        sub_ar.insert(k + 1, expenditure[i])

    return result


def activityNotifications_2(expenditure, d):
    from bisect import insort, bisect_left
    v = sorted(expenditure[: d])
    count = 0
    for i, current in enumerate(expenditure[d:]):
        de = expenditure[i]
        if d % 2 == 0:
            if current >= v[d // 2] + v[d // 2 - 1]:
                count += 1
        elif current >= v[d // 2] * 2:
            count += 1
        ix = bisect_left(v, de)
        del v[ix]
        insort(v, current)
    return count


case_1 = [2, 3, 4, 2, 3, 6, 8, 4, 5]  # 2
days_1 = 5
case_2 = [1, 2, 3, 4, 4]  # 0
days_2 = 4

# print(activityNotifications(case_1, days_1))
# print(activityNotifications(case_2, days_2))


##############################################################
# https://www.hackerrank.com/challenges/sherlock-and-anagrams

from collections import Counter


def sherlockAndAnagrams(s):
    count = 0
    for i in range(1, len(s) + 1):
        a = ["".join(sorted(s[j:j + i])) for j in range(len(s) - i + 1)]
        b = Counter(a)
        for j in b:
            count += b[j] * (b[j] - 1) / 2
    return int(count)


##############################################################
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
def minimumAbsoluteDifference(given_arr):
    ar_len = len(given_arr)
    given_arr.sort()
    result = abs(given_arr[0] - given_arr[1])
    for i in range(1, ar_len - 1):
        next_val = abs(given_arr[i] - given_arr[i + 1])
        result = min(next_val, result)
    return result


##############################################################
# https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms

def luckBalance(k, contests):
    result = 0
    dic_helper = {
        0: [],
        1: []
    }

    for item in contests:
        dic_helper[item[1]].append(item[0])

    result = sum(dic_helper[0])
    need_win = sorted(dic_helper[1])
    lose_len = len(need_win) - k
    if lose_len > 0:
        result -= sum(need_win[:lose_len])
    result += sum(need_win[lose_len:])
    return result


case_1 = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]


# print(luckBalance(3, case_1))

##############################################################
# Flipping bits
# https://www.hackerrank.com/challenges/flipping-bits/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous

def flippingBits(n):
    max_int = 2 ** 32 - 1
    result = (max_int & ~n)
    return result


##############################################################
# PracticeAlgorithmsGreedyCandies
# Candies
# https://www.hackerrank.com/challenges/candies/copy-from/143930711

def candies(n, arr):
    minArr1 = [1 for i in range(n)]
    minArr2 = [1 for i in range(n)]
    finalArr = []

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            minArr1[i] = minArr1[i - 1] + 1
        else:
            minArr1[i] = 1

    for j in range(len(arr) - 2, -1, -1):
        if arr[j] > arr[j + 1]:
            minArr2[j] = minArr2[j + 1] + 1
        else:
            minArr2[j] = 1

    for i in range(len(arr)):
        finalArr.append(max(minArr1[i], minArr2[i]))

    return sum(finalArr)


############################
# Find the nearest clone
# https://www.hackerrank.com/challenges/find-the-nearest-clone/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=graphs

import itertools


# initial approach
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    result = -1

    node_dic = {(key + 1): set() for key in range(graph_nodes)}
    color_dic = {key: set() for key in ids}

    for i in range(len(graph_from)):
        from_val = graph_from[i]
        to_val = graph_to[i]
        node_dic[from_val].add(to_val)
        node_dic[to_val].add(from_val)

    for i in range(graph_nodes):
        color = ids[i]
        color_dic[color].add(i + 1)

    color_nodes = color_dic[val]
    pre_result = 0
    pas_dic = {(key): set([key]) for key in color_nodes}
    visited = 1
    while visited < graph_nodes:
        pre_result += 1
        visited_ar = []
        for key, val in pas_dic.items():
            new_set = set()
            for dep in val:
                new_set.update(node_dic[dep])
            pas_dic[key].update(new_set)
            visited_ar.append(len(pas_dic[key]))

        for key, val in pas_dic.items():
            for node in val:
                if node != key and node in color_nodes:
                    return pre_result
        visited = min(visited_ar)
    return result


# optimized solution
from collections import deque


class Node:
    def __init__(self, index):
        self.index = index
        self.neighbors = set()

    def conn(self, other):
        self.neighbors.add(other)
        other.neighbors.add(self)


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    nodes = {i + 1: Node(i + 1) for i in range(graph_nodes)}
    for start, end in zip(graph_from, graph_to):
        nodes[start].conn(nodes[end])

    queue = deque()
    visited = {}

    for i, id in enumerate(ids):
        if id == val:
            visited[i + 1] = (i + 1, 0)
            queue.append(nodes[i + 1])

    while queue:
        current = queue.popleft()
        source, path_len = visited[current.index]

        for n in current.neighbors:
            if n.index not in visited:
                visited[n.index] = (source, path_len + 1)
                queue.append(n)
            else:
                if visited[n.index][0] == source:
                    continue
                return path_len + visited[n.index][1] + 1

    return -1


# Case 0
graph_nodes = 4
graph_from = [1, 1, 4]
graph_to = [2, 3, 2]
ids = [1, 2, 1, 1]
val = 1  # 1

# Case 1
graph_nodes = 4
graph_from = [1, 1, 4]
graph_to = [2, 3, 2]
ids = [1, 2, 3, 4]
val = 2  # -1

# Case 2
graph_nodes = 5
graph_from = [1, 1, 2, 3]
graph_to = [2, 3, 4, 5]
ids = [1, 2, 3, 3, 2]
val = 2  # 3

# print(findShortest(graph_nodes, graph_from, graph_to, ids, val))

#####################################################################################
# Frequency Queries
# https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps

import collections

def Frequency_Queries():
    def freqQuery_slow(queries):
        result = collections.deque()
        data_dic = collections.defaultdict(int)
        for opertion, val in queries:
            if opertion == 1:
                data_dic[val] += 1
            elif opertion == 2:
                data_dic[val] = 0 if data_dic[val] == 0 else data_dic[val] - 1
            else:
                result.append(0)
                for key, val_0 in data_dic.items():
                    if val_0 == val:
                        result.pop()
                        result.append(1)
                        break
        return list(result)


    def freqQuery(queries):
        result = collections.deque()
        data_dic = collections.defaultdict(int)
        counter_dic = collections.defaultdict(int)
        for opertion, val in queries:
            if opertion == 1:
                if data_dic[val] != 0:
                    counter_dic[data_dic[val]] -= 1
                data_dic[val] += 1
                counter_dic[data_dic[val]] += 1
            elif opertion == 2:
                if data_dic[val] != 0:
                    counter_dic[data_dic[val]] -= 1
                data_dic[val] = 0 if data_dic[val] == 0 else data_dic[val] - 1
                if data_dic[val] != 0:
                    counter_dic[data_dic[val]] += 1
            else:
                if counter_dic[val] == 0:
                    result.append(0)
                else:
                    result.append(1)

        return list(result)

    # Case2 [0, 1, 1]
    queries = [[1, 3], [2, 3], [3, 2], [1, 4], [1, 5], [1, 5], [1, 4], [3, 2], [2, 4], [3, 2]]

    # Case1 [0, 1]
    queries = [[3, 4], [2, 1003], [1, 16], [3, 1]]

    # Case0 [0, 1]
    queries = [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]

    print(freqQuery(queries))


#####################################################################################
# https://www.hackerrank.com/challenges/largest-rectangle/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues
# Largest Rectangle

def LargestRectangle():
    from collections import deque


    def largestRectangle(histogram):
        areas_stack = deque()
        index = 0
        max_area = 0
        while index < len(histogram):
            if len(areas_stack) == 0 or \
                    histogram[areas_stack[-1]] <= histogram[index]:

                areas_stack.append(index)
                index += 1

            else:
                prev_index = areas_stack.pop()
                current_area = histogram[prev_index] * ((index - areas_stack[-1] - 1) if areas_stack else index)

                max_area = max(current_area, max_area)

        while areas_stack:
            prev_index = areas_stack.pop()

            current_area = (histogram[prev_index] *
                    ((index - areas_stack[-1] - 1)
                     if areas_stack else index))

            # update max area, if needed
            max_area = max(max_area, current_area)

        return max_area

    case_1 = [1, 2, 3, 4, 5] # 9
    print(largestRectangle(case_1))



#####################################################################################
# Recursive Digit Sum
# https://www.hackerrank.com/challenges/recursive-digit-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=recursion-backtracking

from Companies.util_decorators import timeit

def RecursiveDigitSum():
    @timeit
    def superDigit(num_val, factor):
        num_str = str(num_val)
        num_str = str(sum(int(s) for s in num_str) * factor)
        result = 0
        while len(num_str) > 1:
            num_str = str(sum(int(x) for x in num_str))

        result += int(num_str)

        return result


    def superDigitRecursive(n, k):
        def add_digits(string):
            if len(string) == 1:
                return string
            result = sum(int(s) for s in string)
            return add_digits(str(result))

        start = sum(int(s) for s in n) * k
        return add_digits(str(start))

    print(superDigit(148, 3)) # 3

#####################################################################################
# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup
# Sock Merchant

def SockMerchant():
    from collections import defaultdict

    # Complete the sockMerchant function below.
    def sockMerchant(n, sock_ar):
        result = 0
        sock_dic = defaultdict(int)
        for color in sock_ar:
            sock_dic[color] += 1
            if sock_dic[color] == 2:
                result += 1
                sock_dic[color] = 0

        return result

#####################################################################################
# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists
# Reverse a doubly linked list


def Reverseadoublylinkedlist():
    def reverse(head):
        current_node = head
        last = head
        while current_node:
            last = current_node
            current_node.next, current_node.prev = current_node.prev, current_node.next
            current_node = current_node.prev

        return last

#####################################################################################