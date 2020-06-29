# Hack the Interview V (U.S.)
#

#################################################################################################
# https://www.hackerrank.com/contests/hack-the-interview-v/challenges/strange-keyboard-1
# New Keyboard 10 points , 100%

def _receivedText(S):
    numlock_on = True
    d_q = []
    index = 0
    for val in S:
        if val == "*":
            if index > 0:
                index -= 1
                d_q.pop(index)
        elif val == "#":
            numlock_on = not numlock_on
        elif val == "<":
            index = 0
        elif val == ">":
            index = len(d_q)
        else:
            if not numlock_on and val in "1234567890":
                pass
            else:
                d_q.insert(index, val)
                index += 1

    result = "".join(d_q)
    return result


class Node:
    def __init__(self, val="", parent=None, child=None):
        self.val = val
        self.parent = parent
        self.child = child


def receivedText(S):
    if len(S) < 1000:
        return _receivedText(S)
    numlock_on = True

    left_end = Node()
    right_end = Node()
    left_end.child = right_end
    right_end.parent = left_end
    current = left_end
    for val in S:
        if val == "*":
            if current != left_end:
                current.parent.child = current.child
                current.child.parent = current.parent
                current = current.parent
        elif val == "#":
            numlock_on = not numlock_on
        elif val == "<":
            current = left_end
        elif val == ">":
            current = right_end.parent
        else:
            if not numlock_on and val in "1234567890":
                pass
            else:
                new_node = Node(val, current, current.child)
                current.child = new_node
                current = new_node

    # result = [""] * len(S)
    # i = 0
    # while left_end:
    #     result[i] = left_end.val
    #     left_end = left_end.child
    #     i += 1
    result = []
    while left_end:
        result.append(left_end.val)
        left_end = left_end.child
    result = "".join(result)
    return result


# print(receivedText("HE*<LR>O")) # LLHO

#################################################################################################
# https://www.hackerrank.com/contests/hack-the-interview-v/challenges/the-xor-problem
# The XOR Problem - 20 points, 100%

def maxXorValue(x, k):
    result = ["0"] * len(x)

    for i, val in enumerate(x):
        if k == 0:
            break
        if val == "0":
            result[i] = "1"
            k -= 1

    result = "".join(result)
    return result

# print(maxXorValue("10010", 5)) # 01101
#
# print(maxXorValue("01010", 1)) # 10000

#################################################################################################
# https://www.hackerrank.com/contests/hack-the-interview-v/challenges/candy-crush-4
# Jewel Game - 30 points 100%

from collections import deque

def getMaxScore(jewels):
    score = 0

    if len(jewels) > 1:
        d_q = deque()
        end = 0
        while end < len(jewels):
            if not d_q:
                d_q.append(jewels[end])
                end += 1
            else:
                if d_q[-1] == jewels[end]:
                    score += 1
                    end += 1
                    d_q.pop()
                else:
                    d_q.append(jewels[end])
                    end += 1

    return score

# print(getMaxScore("abcddcbd")) # 3
# print(getMaxScore("abcd")) # 0

#################################################################################################
# https://www.hackerrank.com/contests/hack-the-interview-v/challenges/rerouting/problem
# Rerouting - 20 points = 50%


def _getMinConnectionChange(connection):
    result = 0
    visited = [set(i) for i in len(connection)]
    for i, val in enumerate(connection):
        if visited[i] == 0:
            if visited[val - 1] == 1:
                visited[i] = 1
            else:
                result += 1
                k = i
                while visited[k] == 0:
                    visited[k] = 1
                    k = val - 1
                    val = connection[k]

    return result - 1

class DisjointSet:
    def __init__(self):
        self.parent = self
        self.size = 1

    def find_parent(self):
        if self.parent != self:
            self.parent = self.parent.find_parent()
        return self.parent

    def union(self, other):
        if self == other:
            return
        root = self.find_parent()
        other_root = other.find_parent()
        if root == other_root:
            return
        if root.size > other_root.size:
            other_root.parent = root
            root.size += other_root.size
        else:
            root.parent = other_root
            other_root.size += root.size


def getMinConnectionChange(connection):
    result = 0
    visited_sets = [DisjointSet() for _ in range(len(connection))]
    has_end = False
    for i, val in enumerate(connection):
        has_end = has_end or i == val - 1
        left_val, right_val = i, val - 1
        left_set = visited_sets[left_val]
        right_set = visited_sets[right_val]
        if left_set.size > right_set.size:
            left_set.union(right_set)
        else:
            right_set.union(left_set)

    root_dic = {}
    for set_val in visited_sets:
        if set_val.parent not in root_dic:
            root_dic[set_val.parent] = 1
    if not has_end:
        return len(root_dic)

    return len(root_dic) - 1


def solve(n, connection):
    # Write your code here
    assert 1 <= n <= 300000
    assert all(1 <= i <= n for i in connection)

    vis = [0] * (n + 1)
    ct = 0
    col = 0
    for i in range(1, n + 1):
        if not vis[i]:
            cur = i
            col += 1
            while not vis[cur]:
                vis[cur] = col
                cur = connection[cur - 1]
                ct += col == vis[cur]
    ct -= any(i == connection[i - 1] for i in range(1, n + 1))
    return ct

print(getMinConnectionChange([2, 3, 4, 1, 5]))  # 1
print(getMinConnectionChange([1, 2, 3, 4]))  # 3
print(getMinConnectionChange([2, 3, 4, 1]))  # 1
print(getMinConnectionChange([2, 1, 4, 3, 5]))  # 2
#
print(getMinConnectionChange([1, 3, 4, 4]))  # 1

print(getMinConnectionChange([1, 2, 4, 3]))

#################################################################################################