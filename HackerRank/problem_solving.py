# TODO - clean up here!!!

##############################################
# Maximum Subarray Sum
from bisect import insort, bisect_right

def MaximumSubarraySum():
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
def climbingLeaderboardSolution():
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

def commonChildSolution():
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
def minimumBribesSoluton():
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

def minimumSwapsSolution():
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

def maxSubsetSumSolution():
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

def abbreviationSolution():
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

def PlayerSolution():
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

def activityNotificationsSolution():
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

def luckBalanceSolution():
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

def findShortestSolution():
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

def Frequency_QueriesSolution():
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
# https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists
# Linked Lists: Detect a Cycle

def LinkedListsDetectCycle():
    def has_cycle(head):
        fast = head.next
        slow = head
        while fast and fast != slow:
            slow = slow.next
            fast = fast.next
            if fast:
                 fast = fast.next
        return fast == slow


#####################################################################################
# Jumping on the Clouds
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup

def jumpingOnClouds(c):
    start = 0
    counter = 0
    while start < len(c):
        start += 2
        if start < len(c) and c[start] == 0:
            pass
        else:
          start -= 1
        if start < len(c):
            counter +=1
    return counter

#####################################################################################
# Counting Valley
# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup

def CountingValley():
    import math
    import os
    import random
    import re
    import sys

    # Complete the countingValleys function below.
    def countingValleys(n, s):
        result = 0
        current_level = 0
        for i in s:
            if i == "U":
                current_level += 1
            else:
                if current_level == 0:
                    result += 1
                current_level -= 1
        return result

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        n = int(input())

        s = input()

        result = countingValleys(n, s)

        fptr.write(str(result) + '\n')

        fptr.close()


#####################################################################################
# Forming a Magic Square
# https://www.hackerrank.com/challenges/magic-square-forming/problem

def FormingaMagicSquare():
    def formingMagicSquare(s):
        diffs = []
        all_possible = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]], ]

        # compare s to each in all possible get number of differences for each to diffs
        for possiblity in all_possible:
            cost = 0
            for p_row, s_row in list(zip(possiblity, s)):
                for p_num, s_num in (list(zip(p_row, s_row))):
                    if p_num != s_num:
                        cost += abs(p_num - s_num)
            diffs.append(cost)

        return min(diffs)

    # case 0 - 7 ???
    M = [[5, 3, 4,],
    [1, 5, 8],
    [6, 4, 2]]

    # case 1 - 1
    M = [[4, 9, 2],
    [3, 5, 7],
    [8, 1, 5]]

    # case 2 - 4
    M = [[4, 8, 2],
    [4, 5, 7],
    [6, 1, 6]]

    print(formingMagicSquare(M))

#####################################################################################

from collections import OrderedDict

# Complete the matchingStrings function below.
def matchingStrings_0(strings, queries):
    count_dict = OrderedDict()
    for key in queries:
        count_dict[key] = 0
    for key in strings:
        count_dict[key] += 1

    return count_dict.values()

def matchingStrings(strings, queries):
    count_dict = {}
    for key in queries:
        count_dict[key] = 0
    for key in strings:
        if key in count_dict:
            count_dict[key] += 1

    return [count_dict[val] for val in queries]

#####################################################################################
# https://www.hackerrank.com/challenges/non-divisible-subset/problem
# Non-Divisible Subset

def nonDivisibleSubsetSolution():
    def nonDivisibleSubset(target_val, int_ar):
        result = 0
        div_dic = [0] * target_val
        int_ar = set(int_ar)
        for val in int_ar:
            div_dic[val % target_val] += 1
        mid = int((target_val - 1) / 2)
        for i in range(1, mid + 1):
            result += max(div_dic[i], div_dic[-i])
        if div_dic[0] > 0:
            result += 1
        if (target_val - 1) % 2 > 0 and div_dic[int((target_val - 1)  / 2) + 1] > 0:
            result += 1

        return result

    # Case 1 - 3
    target_val = 3
    int_ar = [1, 7, 2, 4]

    # Case 2 - 3
    target_val = 4
    int_ar = [19, 10, 12, 10, 24, 25, 22]
    print(nonDivisibleSubset(target_val, int_ar))

#####################################################################################
# https://www.hackerrank.com/challenges/contacts/problem
# contacts

# not tree based solution
def contacts_solution():
    def contacts_slow(queries):
        from collections import defaultdict
        result = []
        name_dic = defaultdict(int)
        for item in queries:
            operation = item[0]
            name = item[1]
            if operation == "add":
                key = ''
                for char_val in name:
                    key += char_val
                    name_dic[key] += 1
            elif operation == "find":

                result.append(name_dic[name])
        return result

    #  tree based solution
    from collections import defaultdict

    class NameNode:
        def __init__(self, val=''):
            self.counter = 0
            self.val = val
            self.dic = defaultdict(NameNode)

    def contacts(queries):

        result = []
        root_node = NameNode()
        for item in queries:
            operation = item[0]
            name = item[1]

            if operation == "add":
                current_node = root_node
                for char_val in name:
                    current_node = current_node.dic[char_val]
                    current_node.val = char_val
                    current_node.counter += 1

            elif operation == "find":
                current_node = root_node
                current_val = 0
                for char_val in name:
                    current_node = current_node.dic[char_val]
                    current_val = current_node.counter

                result.append(current_val)
        return result

    # case 1 - 2 0
    queries = [
    ["add", "hack"],
    ["add", "hackerrank"],
    ["find", "hac"],
    ["find", "hak"]]
    print(contacts(queries))

     # case 2 -
    queries = [
    ["add", 's'],
    ["add", "ss"],
    ["add", "sss"],
    ["add", "ssss"],
    ["add", 'sssss'],
    ["find", "s"],
    ["find", "ss"],
    ["find", "sss"],
    ["find", "ssss"],
    ["find","sssss"],
    ["find", "ssssss"]]

    print(contacts(queries))

#####################################################################################
# https://www.hackerrank.com/challenges/queens-attack-2/problem?h_r=internal-search
# Queen's Attack II

def queensAttack_Solution():
    from collections import defaultdict

    # obstacles = [(x, y)]

    def queensAttack(board_size, obs_count, row_q, col_q, obstacles):
        result = 0
        start_point = (row_q, col_q)
        obstacles_dic = defaultdict(set)
        for row, col in obstacles:
            obstacles_dic[row].add(col)
        delta_ar = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

        for delta in delta_ar:
            result += _track_counter(board_size, start_point, delta,obstacles_dic)

        return result

    def _track_counter(board_size, start_point, delta, obstacles_dic):
        result = 0
        row = start_point[0]
        col = start_point[1]
        while True:
            row += delta[0]
            col += delta[1]
            if row < 1 or row > board_size or col < 1 or col > board_size or col in obstacles_dic[row]:
                break
            else:
                result += 1
        return result

    board_size = 4
    obs_count = 0
    row_q = 4
    col_q = 4
    obstacles = []
    print(queensAttack(board_size, obs_count, row_q, col_q, obstacles))

#####################################################################################
# https://www.hackerrank.com/challenges/countingsort4/problem
# The Full Counting Sort

def TheFullCountingSortSolution():
    from collections import defaultdict

    def countSort(arr):
        # max_num = 10
        # result = [[] for _ in range()]
        result = []
        word_dic = defaultdict(list)
        mid = int(len(arr) / 2)
        max_key = 0
        for i, item in enumerate(arr):
            key, val = item
            key = int(key)
            max_key = max(max_key, key)
            if i < mid:
                word_dic[key].append('-')
            else:
                word_dic[key].append(val)

        result = [" ".join(word_dic[i]) for i in range(max_key + 1) if word_dic[i]]
        print(" ".join(result))

    arr = [
        ["1","e"],
        ["2", "a"],
        ["1", "b"],
       ["3", "a"],
       ["4", "f"],
        ["1", "f"],
        ["2", "a"],
        ["1", "e"],
        ["1", "b"],
        ["1", "c"]]

    countSort(arr)
#####################################################################################
# https://www.hackerrank.com/challenges/find-maximum-index-product/problem
# Find Maximum Index Product

def FindMaximumIndexProduct():
    from collections import deque

    def solve(arr):
        result = 0
        result_left = [0] * len(arr)
        result_right = [0] * len(arr)

        stack_max = deque()
        stack_max.append(0)

        for i in range(1, len(arr) - 1):
            while stack_max:
                if arr[i] < arr[stack_max[-1]]:
                    result_left[i] = stack_max[-1] + 1
                    stack_max.append(i)
                    break
                stack_max.pop()
            else:
                stack_max.append(i)
                result_left[i] = 0

        stack_max = deque()
        stack_max.append(len(arr) - 1)
        for i in range(len(arr) - 2, 0, -1):
            while stack_max:
                if arr[i] < arr[stack_max[-1]]:
                    result_right[i] = stack_max[-1] + 1
                    stack_max.append(i)
                    break
                stack_max.pop()
            else:
                stack_max.append(i)
                result_right[i] = 0

        for i in range(0, len(arr)):
            result = max(result_right[i] * result_left[i], result)
        return result

    # case 1
    arr = [5, 4, 3, 4, 5] # 8
    print(solve(arr))

    # case 2
    arr = [1, 1, 0, 1, 1] # 8
    print(solve(arr))

#####################################################################################
# https://www.hackerrank.com/challenges/count-luck/problem
# Count Luck


def CountLuckSolution():
    from collections import deque


    def countLuck(matrix, k):
        result = 0
        # delta = [(-1,0), (1,0), (0, -1), (0, 1)]
        START_POINT = "M"
        END_POINT = "*"
        BLOCK_POINT = "X"

        start = () # row, col
        end = ()
        row_num = len(matrix)
        col_num = len(matrix[0])
        for i in range(row_num):
            for j in range(col_num):
                if matrix[i][j] == START_POINT:
                    start = (i, j)

        path_q = deque([start])
        turn_dic = {}
        turn_dic[start] = 0
        while not end and path_q:
            top_step = None
            down_step = None
            right_step = None
            left_step = None
            current_step = path_q.popleft()
            step_row, step_col = current_step # [row, col]
            matrix[step_row][step_col] = "X"
            len_before = len(path_q)

            if step_row > 0:
                top_step = (step_row - 1, step_col)
                val = matrix[top_step[0]][top_step[1]]
                if val == END_POINT:
                    end = top_step
                    path_q.append(end)
                elif val != BLOCK_POINT:
                    path_q.append(top_step)

            if step_row < row_num - 1:
                down_step = (step_row + 1, step_col)
                val = matrix[down_step[0]][down_step[1]]
                if val == END_POINT:
                    end = down_step
                    path_q.append(end)
                elif val != BLOCK_POINT:
                    path_q.append(down_step)

            if step_col > 0:
                left_step = (step_row, step_col - 1)
                val = matrix[left_step[0]][left_step[1]]
                if val == END_POINT:
                    end = left_step
                    path_q.append(end)
                elif val != BLOCK_POINT:
                    path_q.append(left_step)

            if step_col < col_num - 1:
                right_step = (step_row, step_col + 1)
                val = matrix[right_step[0]][right_step[1]]
                if val == END_POINT:
                    end = right_step
                    path_q.append(end)
                elif val != BLOCK_POINT:
                    path_q.append(right_step)

            turn = 1 if (len(path_q) - len_before) > 1 else 0

            if down_step:
                turn_dic[down_step] = turn_dic[current_step] + turn
            if top_step:
                turn_dic[top_step] = turn_dic[current_step] + turn
            if right_step:
                turn_dic[right_step] = turn_dic[current_step] + turn
            if left_step:
                turn_dic[left_step] = turn_dic[current_step] + turn

        result = turn_dic[end]

        return "Impressed" if result == k else "Oops!"

    # case 1
    matrix = [
        ["*", ".", "M"],
        [".", "X", "."]
    ]
    print(countLuck(matrix, 1)) # "Impressed"

    # case 2
    matrix = [
        list(".X.X......X"),
        list(".X*.X.XXX.X"),
        list(".XX.X.XM..."),
        list("......XXXX."),
    ]
    print(countLuck(matrix, 3)) # "Impressed"

    # case 3
    matrix2 = [
         list("*.."),
         list("X.X"),
         list("..M")
     ]
    print(countLuck(matrix2, 1)) # "Oops"

#####################################################################################
# https://www.hackerrank.com/challenges/even-tree/problem
# Even Tree

def EvenTree():
    from collections import deque

    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.parent = None
            self.childs = deque()
            self.childCount = 0
            self.parentCount = 0


    def calc_child_count(node):
        if len(node.childs) > 0:
            sum = 0
            for child in node.childs:
                sum += calc_child_count(child)
            node.childCount = sum + len(node.childs)
            return node.childCount
        else:
            node.childCount = 0
            return 0


    def evenForest(t_nodes, t_edges, t_from, t_to):
        result = 0
        all_nodes = [None] * t_nodes

        for i in range(t_nodes):
            all_nodes[i] = TreeNode(i + 1)

        for i in range(t_edges):
            from_val = t_from[i] - 1
            to_val = t_to[i] - 1
            all_nodes[from_val].parent = all_nodes[to_val]
            all_nodes[to_val].childs.append(all_nodes[from_val])

        calc_child_count(all_nodes[0])
        result = len([node for node in all_nodes if (len(node.childs) + 1) % 2 == 0 and node.parent])
        # all_childs = [node for node in all_nodes if len(node.childs) == 0]
        # all_parents = set([node.parent for node in all_childs])
        #
        # while all_parents:
        #     for parent in all_parents:
        #         if (parent.childCount + 1) % 2 == 0:
        #             result += 1
        #     all_parents = set([node.parent for node in all_parents if node.parent and node.parent.parent])

        return result


    # case 1
    t_nodes = 10
    t_edges = 9
    t_from = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    t_to = [1, 1, 3, 2, 1, 2, 6, 8, 8]
    print(evenForest(t_nodes, t_edges, t_from, t_to))

    # case 2 = 4
    t_nodes = 20
    t_edges = 19
    t_from = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    t_to =   [1, 1, 3, 2, 5, 1, 1, 2, 7, 10, 3, 7, 8, 12, 6, 6, 10, 1, 8]
    print(evenForest(t_nodes, t_edges, t_from, t_to))

import os
import sys


# it wont work for random order of nodes edges
def another_solusion():
    tree_nodes, tree_edges = map(int, input().split())

    tree_from = [0] * tree_edges
    tree_to = [0] * tree_edges

    for tree_itr in range(tree_edges):
        tree_from[tree_itr], tree_to[tree_itr] = map(int, input().split())

    tree_weight = {}
    for tree_itr in range(tree_edges - 1, -1, -1):
        if tree_from[tree_itr] in tree_weight:
            tree_weight[tree_from[tree_itr]] += 1
        else:
            tree_weight[tree_from[tree_itr]] = 1
        if tree_to[tree_itr] in tree_weight:
            tree_weight[tree_to[tree_itr]] += tree_weight[tree_from[tree_itr]]
        else:
            tree_weight[tree_to[tree_itr]] = tree_weight[tree_from[tree_itr]]
    # print(tree_weight)
    print(len([1 for key in tree_weight if tree_weight[key] % 2 == 0]))

#####################################################################################
# https://www.hackerrank.com/challenges/truck-tour/problem
# Truck Tour
# good one, simple beautiful solution

from collections import deque

def TruckTour():
    def truckTour(petrolpumps):
        if len(petrolpumps) == 1:
            return 0
        start = 0
        current_ind = 0
        current_sum = 0
        while current_ind > start - 1:
            if current_sum >= 0:
                next_val = petrolpumps[current_ind][0] - petrolpumps[current_ind][1]
                current_ind = current_ind + 1 if current_ind < len(petrolpumps) - 1 else 0
                current_sum += next_val
            else:
                current_sum = current_sum - petrolpumps[start][0] + petrolpumps[start][1]
                start += 1

        return start


    petrolpumps = [[1, 5], [10, 3], [3, 4]]
    print(truckTour(petrolpumps))

#####################################################################################
# https://www.hackerrank.com/challenges/is-binary-search-tree/problem
# Is This a Binary Search Tree?


def BinarySearchTree():
    """ Node is defined as
    class node:
      def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None
    """
    def check_binary_search_tree_(root):
        result = True
        result = result and __check_binary_recursive(root.left, -1, root.data)
        result = result and __check_binary_recursive(root.right, root.data, 10**5)
        return result

    def __check_binary_recursive(root, min_val, max_val):
        if not root:
            return True
        if root.data > min_val and root.data < max_val:
            return __check_binary_recursive(root.left, min_val, root.data) and \
                   __check_binary_recursive(root.right, root.data, max_val)
        else:
            return False

#####################################################################################