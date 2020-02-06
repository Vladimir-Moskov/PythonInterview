#############################################
# https://www.hackerrank.com/challenges/string-reduction/problem


def stringReduction_bad(given_str):
    chat_dic = {
        'a': {
            'b': 'c',
            'c': 'b'
        },
        'b': {
            'a': 'c',
            'c': 'a'
        },
        'c': {
            'b': 'a',
            'a': 'b'
        },
    }

    str_ar = list(given_str)
    if len(str_ar) < 2:
        return len(str_ar)
    start_index = 0

    while start_index < (len(str_ar) - 1):
        cur_char = str_ar[start_index]
        next_char = str_ar[start_index + 1]
        if cur_char == next_char:
            start_index += 1
        else:
            new_char = chat_dic[cur_char][next_char]
            str_ar[start_index + 1] = new_char
            str_ar.pop(start_index)
            start_index = max(0, start_index - 1)

    result = len(str_ar)
    return result


def stringReduction(given_str):
    from collections import Counter, defaultdict
    char_count = Counter(given_str)
    if len(char_count) == 1:
        return len(given_str)
    else:
        all_odd_even = char_count.get('a', 0) % 2 + char_count.get('b', 0) % 2 + char_count.get('c', 0) % 2
        if all_odd_even == 0 or all_odd_even == 3:
            return 2
        else:
            return 1


case_0 = "abcbcba"  # 0
case_1 = "aab"  # 2
case_2 = "bcab"  # 1
case_3 = "ccccc"  # 5
case_4 = "babcbbaabcbcbcbaabbccaacccbbbcaaacabbbbaaaccbcccacbbccaccbbaacaccbabcaaaacaccacbaacc"  #
case_5 = "acaacababbcbabbbbbaaaabacaabbcbac"
case_6 = "bcbcacacbbaaccbaacbccaca"
# print(stringReduction(case_0))
# print(stringReduction(case_1))
# print(stringReduction(case_2))
# print(stringReduction(case_3))
# print(stringReduction(case_4))
# print(stringReduction(case_5))
# print(stringReduction(case_6))

#########################################################
# Common Child
# https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

def commonChild_bad(str_val_1, str_val_2):
    mach_matrix = [[0 for _ in range(len(str_val_1) + 1)] for _ in range(len(str_val_2) + 1)]
    for j, char_2 in enumerate(str_val_2, 1):
        for i, char_1 in enumerate(str_val_1, 1):
            if char_1 == char_2:
                mach_matrix[j][i] = mach_matrix[j - 1][i - 1] + 1
            else:
                mach_matrix[j][i] = max(mach_matrix[j-1][i], mach_matrix[j][i-1])

    result = mach_matrix[-1][-1]

    return result

def commonChild(s1, s2):
    m, n = len(s1), len(s2)
    prev, cur = [0]*(n+1), [0]*(n+1)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                cur[j] = 1 + prev[j-1]
            else:
                if cur[j-1] > prev[j]:
                    cur[j] = cur[j-1]
                else:
                    cur[j] = prev[j]
        cur, prev = prev, cur
    return prev[n]


case_00 = "TERRACED"  # 5
case_00_2 = "CRATERED"
case_0 = "HARRY"  # 2
case_0_2 = "SALLY"
case_1 = "SHINCHAN"  # 3
case_1_2 = "NOHARAAA"
case_2 = "ABCDEF"
case_2_2 = "FBDAMN"  # 2
case_3 = "AA"
case_3_2 = "BB"  # 0
#
case_4 = "WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS"
case_4_2 = "FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC"  # 15

# print(commonChild(case_00, case_00_2))
# print(commonChild(case_0, case_0_2))
# print(commonChild(case_1, case_1_2))
# print(commonChild(case_2, case_2_2))
# print(commonChild(case_3, case_3_2))
# print(commonChild(case_4, case_4_2))


# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
# Hash Tables: Ice Cream Parlor


def whatFlavors_slow(cost, money):
    len_cost = len(cost)
    for i in range(len_cost - 1):
        if cost[i] < money:
            for j in range(i + 1, len_cost):
                if cost[j] < money and money == (cost[i] + cost[j]):
                    break
        if money == (cost[i] + cost[j]):
            break
    return f"{i+1} {j+1}"


def whatFlavors_no(cost, money):
    len_cost = len(cost)
    dic = {}
    for i in range(len_cost):
        dic[cost[i]] = i
    cost.sort()
    for i in range(len_cost - 1):
        el_i = cost[i]
        for j in range(i + 1, len_cost):
            if money < (el_i + cost[j]):
                j -= 1
                break
        if money == (el_i + cost[j]):
            break

    return f"{dic[cost[i]] + 1} {dic[cost[j]] + 1}"


def whatFlavors(cost, money):
    prce_dic = {}
    for i, cost in enumerate(cost):
        rest = money - cost
        if rest > 0:
            if prce_dic.get(rest, 0) != 0:
                return f"{prce_dic[rest]} {i + 1}"
            else:
                prce_dic[cost] = i + 1

    return ""


case_1 = [1, 4, 5, 3, 2]
money_1 = 4  # 1 4
case_2 = [2, 2, 4, 3]
money_2 = 4  # 1 2

# print(whatFlavors(case_1, money_1))
# print(whatFlavors(case_2, money_2))

########################################################



#######################################
# https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
def triplets(arr_a, arr_b, arr_c):
    def index_max(set_int, val, start_index):
        set_len = len(set_int)
        for i in range(start_index, set_len):
            set_val = set_int[i]
            if set_val > val:
                return i
        return set_len

    result = 0
    set_a = sorted(set(arr_a))
    set_b = sorted(set(arr_b))
    set_c = sorted(set(arr_c))
    a_index = 0
    c_index = 0
    for val_b in set_b:
        a_index = index_max(arr_a, val_b, a_index)
        c_index = index_max(arr_c, val_b, c_index)
        result += a_index * c_index

    return result

# 8
case_1_1 = [1, 3, 5]
case_1_2 = [2, 3]
case_1_3 = [1, 2, 3]

# 5
case_2_1 = [1, 4, 5]
case_2_2 = [2, 3, 3]
case_2_3 = [1, 2, 3]

# 12
case_3_1 = [1, 3, 5, 7]
case_3_2 = [5, 7, 9]
case_3_3 = [7, 9, 11, 13]
# print(triplets(case_1_1, case_1_2, case_1_3))
# print(triplets(case_2_1, case_2_2, case_2_3))
# print(triplets(case_3_1, case_3_2, case_3_3))

#######################################
#######################################
# Castle on the Grid
# https://www.hackerrank.com/challenges/castle-on-the-grid/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues


def minimumMoves(grid, startX, startY, goalX, goalY):
    """
    Breath first algorithm
    :param grid:
    :param startX:
    :param startY:
    :param goalX:
    :param goalY:
    :return:
    """
    valid_step = '.'
    invalid_step = 'X'

    # edge cases
    if grid[startX][startY] == invalid_step or\
        grid[goalX][goalY] == invalid_step :
        return -1
    if startX == goalX and startY == goalY:
        return 0

    from collections import deque, namedtuple
    result = 0
    Point = namedtuple("Point", 'x, y')
    steps_queue = deque()
    grid_size = len(grid)
    visited_matrix = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    start_point = Point(startY, startX)
    visited_matrix[start_point.y][start_point.x] = 1
    steps_queue.append(start_point)
    end_point = Point(goalY, goalX)
    def get_next_step(step, delta_x, delta_y, end_step):

        next_step = Point(step.x + delta_x, step.y + delta_y)
        while next_step.x >= 0 and next_step.y >= 0 and \
            next_step.x < grid_size and next_step.y < grid_size:
            if visited_matrix[next_step.y][next_step.x] == 1:
                break
            visited_matrix[next_step.y][next_step.x] = 1
            if grid[next_step.y][next_step.x] == valid_step:
                if next_step.x == end_step.x and next_step.y == end_step.y:
                    return 1
                steps_queue.append(next_step)
            else:
                break
            next_step = Point(next_step.x + delta_x, next_step.y + delta_y)

        return 0

    while len(steps_queue) > 0:

        cur_steps = list(steps_queue)
        steps_queue.clear()
        result += 1
        for current_step in cur_steps:
            # get next steps

            is_done = get_next_step(current_step, 0, -1, end_point)
            if is_done:
                return result

            is_done = get_next_step(current_step, 0, 1, end_point)
            if is_done:
                return result

            is_done = get_next_step(current_step, -1, 0, end_point)
            if is_done:
                return result

            is_done = get_next_step(current_step, 1, 0, end_point)
            if is_done:
                return result

    return result

def minimumMoves_good(grid, startY, startX, goalY, goalX):
    from collections import deque
    q = deque()
    q.append((startX, startY, 0, -1))
    visited = {(startY, startX): 0}
    x, y = [-1, 0, 0, 1, 1], [0, 1, -1, 0, 1]
    def is_valid(x, y, new_dist):
        return x < len(grid) and y < len(grid) and x >= 0 and y >= 0 and grid[y][x] == '.' and ((y, x) not in visited or ((y, x) in visited and new_dist <= visited[(y, x)]))
    while q:
        n = q.pop()
        for k in range(4):
            dist = 0 if (x[k], y[k]) == (x[n[3]], y[n[3]]) else 1
            if is_valid(n[0] + x[k], n[1] + y[k], n[2] + dist):
                visited[(n[1] + y[k], n[0] + x[k])] = n[2] + dist
                q.appendleft((n[0] + x[k], n[1] + y[k], n[2] + dist, k))
    return visited[(goalY ,goalX)]
# 3
_grid = ['.X.', '.X.', '...']
startX, startY = 0, 0
goalX, goalY = 0, 2
# print(minimumMoves(case_1_grid, startX, startY, goalX, goalY))

# 2
case_1_grid = ['...', '.X.', '.X.']
startX, startY = 2, 0
goalX, goalY = 0, 2
# print(minimumMoves(case_1_grid, startX, startY, goalX, goalY))


###########################################################################
# Balanced Brackets
# https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

def isBalanced(s):
    lefts = '{[('
    rights = '}])'
    closes = {a: b for a, b in zip(rights, lefts)}

    stack = []
    for c in s:
        if c in lefts:
            stack.append(c)
        elif c in rights:
            if not stack or stack.pop() != closes[c]:
                return False

    return "NO" if stack else "YES"


def isBalanced_long(given_str):
    """
    Time complexity - O(n)
    :param given_str:
    :return:
    """
    from collections import deque

    result = True
    left_bracket = ('(', '[', '{')
    right_bracket = (')', ']', '}')
    right_to_left_dic = dict(zip(right_bracket, left_bracket))
    bracket_deque = deque()

    if len(given_str) % 2 == 0:
        for bracket in given_str:
            if bracket in left_bracket:
                bracket_deque.append(bracket)
            else:
                if len(bracket_deque) == 0:
                    result = False
                    break
                else:
                    left_br = right_to_left_dic[bracket]
                    prev_br = bracket_deque.pop()
                    if left_br != prev_br:
                        result = False
                        break
    else:
        result = False

    return "YES" if result else "NO"

case_1 = '{[()]}'
case_2 = '{[(])}'
case_3 = '{{[[(())]]}}'

assert isBalanced(case_1), "YES"
assert isBalanced(case_2), "NO"
assert isBalanced(case_3), "YES"

case_1 = '[()][{}()][](){}([{}(())([[{}]])][])[]([][])(){}{{}{[](){}}}()[]({})[{}{{}([{}][])}]'
case_2 = '[()][{}[{}[{}]]][]{}[]{}[]{{}({}(){({{}{}[([[]][[]])()]})({}{{}})})}'
case_3 = '(])[{{{][)[)])(]){(}))[{(})][[{)(}){[(]})[[{}(])}({)(}[[()}{}}]{}{}}()}{({}](]{{[}}(([{]'
case_4 = '){[]()})}}]{}[}}})}{]{](]](()][{))])(}]}))(}[}{{)}{[[}[]'

print(isBalanced(case_1))
print(isBalanced(case_2))
print(isBalanced(case_3))
print(isBalanced(case_4))

##################################
# Friend Circle Queries
# https://www.hackerrank.com/challenges/friend-circle-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous

def maxCircle_faster(queries):
    elems  = {} # reference for which set they are in
    groups = {} # collection of the sets
    results = []
    maxl = 0
    for a,b in queries:
        if a not in elems:
            groups[a] = set([a])
            elems[a] = a
        if b not in elems:
            groups[b] = set([b])
            elems[b] = b
        if elems[a] != elems[b]:
            a,b =elems[a],elems[b]
            if len(groups[b])>len(groups[a]): a,b=b,a
            groups[a] |= groups[b]
            for p in groups[b]: elems[p] = a
            del groups[b]
        maxl = max(maxl, len(groups[elems[a]]))
        results.append(maxl)
    return results

def maxCircle(queries):
    from collections import deque
    friends_deque = deque()
    friends_deque.append(set(queries[0]))
    max_circle = 2
    queries_len = len(queries)
    result_ar = [max_circle]*queries_len
    for i in range(1, queries_len):
        row = queries[i]
        found = False
        for j, circle in enumerate(friends_deque):
            if row[0] in circle or row[1] in circle:
                found = True
                circle.add(row[0])
                circle.add(row[1])
                max_circle = len(circle)
                if j < len(friends_deque) - 1:
                    for k in range(j + 1, len(friends_deque)):
                        circle_2 = friends_deque[k]
                        if row[0] in circle_2 or row[1] in circle_2:
                            circle.update(circle_2)
                            friends_deque.remove(circle_2)
                            break
                break
        if not found:
            friends_deque.append(set(queries[i]))
        else:
            for circle in friends_deque:
                if len(circle) > max_circle:
                    max_circle = len(circle)
        result_ar[i] = max_circle

    return result_ar


def maxCircle_2(queries):
    """
        optimized version of maxCircle with dictionary instead of set
        :param queries: - matrix of friends 
        :return: 
    """
    dic_helper = {}
    max_circle = 0
    result_ar = []
    for a, b in queries:
        new_set = set()
        new_set.add(a)
        new_set.add(b)
        if a not in dic_helper and b not in dic_helper:
            dic_helper[a] = new_set
            dic_helper[b] = new_set
        else:
            new_set = dic_helper.get(a, set())
            set_b = dic_helper.get(b, set())
            new_set.update(set_b)
            dic_helper[b] = new_set

        max_circle = max(len(new_set), max_circle)
        result_ar.append(max_circle)
    return result_ar

queries_1 =[[1, 2], [3, 4], [2, 3]]

# print(maxCircle(queries_1))
###############################################






































#############################################
