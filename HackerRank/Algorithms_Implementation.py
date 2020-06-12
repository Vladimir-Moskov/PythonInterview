# https://www.hackerrank.com/challenges/grading/problem
# Grading Students


def gradingStudents(grades):
    # Write your code here
    for i, grade in enumerate(grades):
        if grade >= 38:
            rest = grade % 5
            grade += 5 - rest if rest > 2 else 0
            grades[i] = grade
    return grades

############################################################################################
# https://www.hackerrank.com/challenges/kangaroo/problem
# Kangaroo

def kangaroo(x1, v1, x2, v2):
    if x1 > x2 and v1 > v2:
        x1, x2, v1, v2 = x2, x1, v2, v1
    if x1 > x2 and v1 > v2:
        return "NO"
    if x2 > x1 and v2 > v1:
        return "NO"
    if v2 == v1:
        return "NO"
    if (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    return "NO"

############################################################################################
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# Divisible Sum Pairs

def divisibleSumPairs(n, k, ar):
    from collections import defaultdict
    import math
    result = 0
    dic_count = defaultdict(int)
    for i in ar:
        dic_count[i % k] += 1
    for i in range(int(k / 2) + 1):
        if i == 0 or i == k / 2:
            result += (dic_count[i] * (dic_count[i] - 1)) / 2
        else:
            result += dic_count[i] * dic_count[k-i]
    print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))
    return result

############################################################################################
# https://www.hackerrank.com/challenges/electronics-shop/problem
# Electronics Shop


def getMoneySpent(keyboards, drives, s, n, m):
    keyboards.sort(reverse=True)
    drives.sort()
    curr_max = -1
    init_j = 0

    for i in range(n):
        for j in range(init_j, m):
            if keyboards[i] + drives[j] > s:
                init_j = j
                break
            elif keyboards[i] + drives[j] > curr_max:
                curr_max = keyboards[i] + drives[j]

    return curr_max


def getMoneySpentNoSort(keyboards, drives, b):
    prices = [0] * b
    for keyboard in keyboards:
        if keyboard < b:
            prices[keyboard] = -1
    for drive in drives:
        if drive < b:
            if prices[drive] == 1:
                prices[drive] = 1
            else:
                prices[drive] = -2
    i = 1
    j = b - 1
    result = 0
    while i <= j:
        if (prices[i] == -1 or prices[i] == -2) and (prices[j] == 1 or prices[j] == -2):
            result = i + j
            break
        if (prices[i] == -1 or prices[i] == -2) and j >= b -i:
            j -= 1
        else:
            i += 1

    if b > result:
        j = result + 1
        i = b - j
        while i > 0:
            if (prices[i] == -1 or prices[i] == -2) and (prices[j] == 1 or prices[j] == -2):
                result = i + j
                break
            if (prices[i] == 1 or prices[i] == -2)  and j >= b -i:
                j += 1
            else:
                i -= 1
    return -1 if result == 0 else result

# print(getMoneySpent([3, 1], [3, 2, 8], 10))
# print(getMoneySpent([4], [5], 5))

############################################################################################
# https://www.hackerrank.com/challenges/bon-appetit/problem
# Bon Appétit


def bonAppetit(bill, k, b):
    dif = b - (sum(bill) - bill[k]) // 2
    if dif == 0:
        print("Bon Appetit")
    else:
        print(dif)


############################################################################################
# https://www.hackerrank.com/challenges/picking-numbers/problem
# Picking Numbers


def pickingNumbers(given_ar):
    given_ar.sort()
    result = 0
    i = 0
    j = 1
    while j < len(given_ar):
        if given_ar[j] - given_ar[i] < 2:
            j += 1
        else:
            result = max(result, j - i)
            i += 1
    result = max(result, j - i)

    print(pickingNumbers([4, 6, 5, 3, 3, 1]))  # 3
    return result

############################################################################################
# https://www.hackerrank.com/challenges/angry-professor/problem
# Angry Professor


def angryProfessor(k, arrival_times):
    for arrival_time in arrival_times:
        if arrival_time < 1:
            k -= 1
            if k == 0:
                return "NO"
    return "YES"

############################################################################################
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# Beautiful Days at the Movies


def beautifulDays(i, j, k):
    result = 0
    while i <= j:
        original = i
        reversed_num = 0
        num = original
        while num:
            rest = num % 10
            reversed_num = (reversed_num * 10) + rest
            num = num // 10
        print(reversed_num)
        if (original - reversed_num) % k == 0:
            result += 1
        i += 1

    return result

############################################################################################
# https://www.hackerrank.com/challenges/3d-surface-area/problem
# 3D Surface Area


def surfaceArea(A):
    # bottom + top sides
    result = len(A) * len(A[0]) * 2
    result += sum(A[0]) + sum(A[-1])
    result += sum(A[i][0] + A[i][-1] for i in range(len(A)))
    for i in range(len(A)):
        for j in range(len(A[0])):
            if j < len(A[0]) - 1:
                if A[i][j] > A[i][j + 1]:
                    result += A[i][j] - A[i][j + 1]
                else:
                    result += A[i][j + 1] - A[i][j]
            if i < len(A) - 1:
                if A[i][j] > A[i + 1][j]:
                    result += A[i][j] - A[i + 1][j]
                else:
                    result += A[i + 1][j] - A[i][j]

    return result

# A = [[1, 3, 4], [2, 2, 3], [1, 2, 4]]
# print(surfaceArea(A))
#
# some_list = [[1, 3, 4],
#              [2, 2, 3],
#              [1, 2, 4]]
# another_list = [[1, 3, 4], [2, 2, 3], [1, 2, 4]]
# print("Result: %s" % (some_list is list))

############################################################################################
# https://www.hackerrank.com/challenges/two-pluses/problem
# Ema's Supercomputer

def solutionEmaSupercomputer():
    from copy import deepcopy
    from collections import defaultdict
    GOOD = "G"
    BAD = "B"


    def find_max_crosses(width, height, matr):
        result = 0
        result_dic = defaultdict(list)
        result_matrix_left = [[0] * width for _ in range(height)]
        result_matrix_right = [[0] * width for _ in range(height)]
        result_matrix_top = [[0] * width for _ in range(height)]
        result_matrix_bottom = [[0] * width for _ in range(height)]

        for i in range(height):
            for j in range(width):
                if matr[i][j] == 1:
                    if j == 0:
                        result_matrix_left[i][j] = 1
                    else:
                        result_matrix_left[i][j] = 1 + result_matrix_left[i][j - 1]

                    if i == 0:
                        result_matrix_top[i][j] = 1
                    else:
                        result_matrix_top[i][j] = 1 + result_matrix_top[i - 1][j]
                else:
                    result_matrix_left[i][j] = 0
                    result_matrix_top[i][j] = 0

        for i in range(height - 1, -1, -1):
            for j in range(width - 1, -1, -1):
                if matr[i][j] == 1:
                    if j == width - 1:
                        result_matrix_right[i][j] = 1
                    else:
                        result_matrix_right[i][j] = 1 + result_matrix_right[i][j + 1]

                    if i == height - 1:
                        result_matrix_bottom[i][j] = 1
                    else:
                        result_matrix_bottom[i][j] = 1 + result_matrix_bottom[i + 1][j]
                else:
                    result_matrix_right[i][j] = 0
                    result_matrix_bottom[i][j] = 0
        for i in range(height):
                for j in range(width):
                    cur_min = min(result_matrix_left[i][j],  result_matrix_right[i][j],  result_matrix_top[i][j],  result_matrix_bottom[i][j])
                    if result < cur_min:
                        result = cur_min
                        result_dic[result].append((i, j))
        return result, result_dic[result]


    def twoPluses(grid):
        width = len(grid[0])
        height = len(grid)
        matr = [[0] * width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if grid[i][j] == GOOD:
                    matr[i][j] = 1

        prev_max, max_cros = find_max_crosses(width, height, matr)
        next_max = 0
        for cros in max_cros:
            i, j = cros
            next_matr = deepcopy(matr)
            for n in range(prev_max):
                next_matr[i][j - n] = 0
                next_matr[i][j + n] = 0
                next_matr[i - n][j] = 0
                next_matr[i + n][j] = 0
            temp_max, temp = find_max_crosses(width, height, next_matr)
            next_max = max(next_max, temp_max)


        return ((next_max - 1) * 4 + 1) * ((prev_max - 1) * 4 + 1)

    grid = ['GGGGGG', 'GBBBGB', 'GGGGGG', 'GGBBGB', 'GGGGGG']  # 5
    print(twoPluses(grid))
    grid = ['BGBBGB', 'GGGGGG', 'BGBBGB', 'GGGGGG', 'BGBBGB', 'BGBBGB']  # 25
    print(twoPluses(grid))
    grid = ["GBGBGGB",
            "GBGBGGB",
            "GBGBGGB",
            "GGGGGGG",
            "GGGGGGG",
            "GBGBGGB",
            "GBGBGGB"]
    print(twoPluses(grid))  # 45
    grid = [
    "GGGGGGGG",
    "GBGBGGBG",
    "GBGBGGBG",
    "GGGGGGGG",
    "GBGBGGBG",
    "GGGGGGGG",
    "GBGBGGBG",
    "GGGGGGGG"]

    print(twoPluses(grid))  # 81


    from itertools import combinations

    def twoPluses_simple(grid):
      h, w = len(grid), len(grid[0])
      plus = []
      isGood = lambda r, c: grid[r][c] == 'G'
      how = lambda x: 2*x-1
      mm = min(h, w)
      for step in range(1, mm // 2 + (1 if mm % 2 else 0)):
        for r in range(step, h-step):
          for c in range(step, w-step):
            if isGood(r, c):
              s1 = {(r2, c) for r2 in range(r-1, r-step-1, -1) if isGood(r2, c)}
              s2 = {(r2, c) for r2 in range(r+1, r+step+1, +1) if isGood(r2, c)}
              s3 = {(r, c2) for c2 in range(c-1, c-step-1, -1) if isGood(r, c2)}
              s4 = {(r, c2) for c2 in range(c+1, c+step+1, +1) if isGood(r, c2)}
              if len(s1)==step and len(s2)==step and len(s3)==step and len(s4)==step:
                plus.append((how(2*step+1), {(r, c)}|s1|s2|s3|s4))
      if not plus: return 1
      if len(plus) == 1: return plus.pop()[0]
      combs = [s1*s2 for (s1, a), (s2, b) in combinations(plus, 2) if a.isdisjoint(b)]
      return max(combs) if combs else plus.pop()[0]

############################################################################################
# https://www.hackerrank.com/challenges/between-two-sets/problem
# Between Two Sets


def getTotalX(a, b):
    result = 0
    a.sort()
    b.sort()
    start = a[-1]
    end = b[-1]
    while start <= end:
        need_add = True
        for a_val in a:
            if start % a_val != 0:
                need_add = False
                break
        if need_add:
            for b_val in b:
                if b_val % start!= 0:
                    need_add = False
                    break
        if need_add:
            result += 1
            # result.append(start)
        start += 1
    return result

############################################################################################
# https://www.hackerrank.com/challenges/drawing-book/problem
# Drawing Book


def pageCount(n, p):
    n = (n + 2 - n % 2) // 2
    p = p // 2
    left = p
    right = n - p - 1
    return min(left,  right)

# print(pageCount(6, 2)) # 1
# print(pageCount(5, 4)) # 0

############################################################################################
# https://www.hackerrank.com/challenges/beautiful-triplets/problem
# Beautiful Triplets

# O(n) solution
def beautifulTriplets(d, arr):
    result = 0
    if len(arr) < 3:
        return result
    i = 0
    j = 1
    k = 2
    while j < len(arr) - 1:
        first = arr[j] - arr[i]
        if first < d:
            j += 1
        elif first > d:
            if j - i > 1:
                i += 1
            else:
                j += 1
        else:
            k = max(k, j + 1)
            step_back_k = 0
            while k < len(arr):
                second = arr[k] - arr[j]
                if second < d:
                    k += 1
                elif second > d:
                    break
                else:
                    result += 1
                    step_back_k += 1
                    k += 1
            k -= step_back_k
            if j - i > 1:
                i += 1
            else:
                j += 1

    return result

# print(beautifulTriplets(1, [2, 2, 3, 4, 5])) # 3
# print(beautifulTriplets(3, [1, 2, 4, 5, 7, 8, 10])) # 3

# O(n)
from collections import defaultdict, Counter

def beautifulTriplets(d, arr):
    result = 0
    counter = Counter(arr)
    counter = defaultdict(int, counter)
    for i in range(len(arr)):
        result += counter[arr[i]] * counter[arr[i] + d] * counter[arr[i] + d + d]
    return result

############################################################################################
# https://www.hackerrank.com/challenges/encryption/problem
# Encryption
import math

def encryption(s):
    L = len(s)
    s2_from_L = math.sqrt(L)
    row = int(s2_from_L)
    col = math.ceil(s2_from_L)
    while row * col <= L:
        row += 1
    row, col = col, row
    result = [[""] * col for _ in range(row)]

    for i in range(row):
        next = i
        for j in range(col):
            if L > next:
                result[i][j] = s[next]
            else:
                break
            next += row
    return " ".join(["".join(result[j][i] for i in range(col)) for j in range(row)])


# print(encryption("feedthedog"))  # fto ehg ee dd
# print(encryption("haveaniceday"))  # hae and via ecy      isieae fdtonf fotrga anoyec cttctt tfhhhs sieae
# print(encryption("iffactsdontfittotheorychangethefacts")) # isieae fdtonf fotrga anoyec cttctt tfhhhs

############################################################################################
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# Designer PDF Viewer

def designerPdfViewer(h, word):
    a_val = ord('a')
    mav_val = 0
    for ch_val in word:
        mav_val = max(mav_val, h[ord(ch_val) - a_val])

    return mav_val * len(word)


############################################################################################
# https://www.hackerrank.com/challenges/utopian-tree/problem
# Utopian Tree

def utopianTree(n):
    result = 1
    for i in range(n):
        if i % 2 != 0:
            result += 1
        else:
            result *= 2
    return result
############################################################################################
# https://www.hackerrank.com/challenges/strange-advertising/problem
# Viral Advertising

def viralAdvertising(n):
    Shared = 5
    Liked = 2
    result = 2
    for i in range(n - 1):
        Shared = math.floor(Shared / 2) * 3
        Liked = math.floor(Shared / 2)
        result += Liked
    return result

# print(viralAdvertising(5))

############################################################################################
# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
# Jumping on the Clouds: Revisited

def jumpingOnClouds(c, k, n):
    result = 100 #initial energy
    i = k % n #initial jump from 0
    result -= c[i] * 2 + 1 #initial energy loss
    while i != 0:
        i = (i + k) % n
        result -= c[i] * 2 + 1
    return result

############################################################################################
# https://www.hackerrank.com/challenges/minimum-distances/problem
# Minimum Distances

from collections import defaultdict


def minimumDistances(a):
    result = -1
    num_dic = defaultdict(list)
    for i, val in enumerate(a):
        if len(num_dic[val]) < 2:
            num_dic[val].append(i)
        else:
            if num_dic[val][1] - num_dic[val][0] > i - num_dic[val][1]:
                num_dic[val][0] = num_dic[val][1]
                num_dic[val][1] = i
    for val in num_dic.values():
        if len(val) == 2:
            if result == -1:
                result = val[1] - val[0]
            else:
                result = min(result, val[1] - val[0])

    return result

############################################################################################
# https://www.hackerrank.com/challenges/cut-the-sticks/problem
# Cut the sticks


def cutTheSticks(arr):
    result = []
    if len(arr) == 0:
        return result
    arr.sort()
    start = 0
    while start < len(arr):
        sum_val = arr[start]
        result.append(len(arr) - start)
        while start < len(arr) and arr[start] == sum_val:
            start += 1

    return result

# print(cutTheSticks([1, 2, 3])) # [3, 2, 1]
# print(cutTheSticks([5, 4, 4, 2, 2, 8])) # [6, 4, 2, 1]

############################################################################################
# https://www.hackerrank.com/challenges/permutation-equation/problem
# Sequence Equation

def permutationEquation(p):
    result = [0] * len(p)
    sub_p = [0] * len(p)
    for i, val in enumerate(p):
       sub_p[val - 1] = i

    for i in range(len(p)):
        t = sub_p[i]
        t = sub_p[sub_p[i]]
        # t = p[sub_p[sub_p[i]]]
        # result[i] = p[sub_p[sub_p[i]]]
        result[i] = t + 1
    return result


# print(permutationEquation([2, 3, 1]))  #  [2, 3, 1]
# print(permutationEquation([5, 2, 1, 3, 4])) # [4, 2, 5, 1, 3]
# print(permutationEquation([4, 3, 5, 1, 2])) # [1, 3, 5, 4, 2]

############################################################################################
# https://www.hackerrank.com/challenges/chocolate-feast/problem
# Chocolate Feast

def chocolateFeast(n, c, m):
    wrap_count = n // c
    result = wrap_count
    while wrap_count >= m:
        cur_wrap = wrap_count // m
        wrap_count = cur_wrap + wrap_count % m
        result += cur_wrap
    return result

# print(chocolateFeast(15, 3, 2)) # 9


############################################################################################
# https://www.hackerrank.com/challenges/find-digits/problem
# Find Digits


def findDigits(n):
    result = 0
    current_val = n
    while current_val > 0:
        div_val = current_val % 10
        current_val = current_val // 10
        if div_val != 0 and n % div_val == 0:
            result += 1

    return result

# print(findDigits(1012))  # 3