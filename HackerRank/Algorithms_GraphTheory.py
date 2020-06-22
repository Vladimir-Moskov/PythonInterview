##################################################################################
# https://www.hackerrank.com/challenges/bfsshortreach/problem
# Breadth First Search: Shortest Reach

def solutionShortestReach():
    from collections import defaultdict, deque


    def bfs(nodes_num, edges_num, edges, start):
        result = [-1] * (nodes_num + 1)
        edges_dic = defaultdict(list)
        for x, y in edges:
            edges_dic[x].append(y)
            edges_dic[y].append(x)
        result[start] = 0
        dfs_q = deque([start])
        level = 1
        while dfs_q:
            next_q = set()
            while dfs_q:
                node = dfs_q.popleft()
                cur_link = edges_dic[node]
                for link in cur_link:
                    if result[link] == -1:
                        result[link] = 6 * level
                        next_q.add(link)

            dfs_q.extend(next_q)
            level += 1

        if start < nodes_num:
            result = result[1:start] + result[start + 1:]
        else:
            result = result[1:start]
        return result

    n = 4
    m = 2
    edges = [[1, 2], [1, 3]]
    s = 1
    #print(bfs(n, m, edges, s))
    n = 3
    m = 1
    edges = [[2, 3]]
    s = 2

    print(bfs(n, m, edges, s))

##################################################################################
# https://www.hackerrank.com/challenges/primsmstsub/problem
# Prim's (MST) : Special Subtree


def solutionSpecialSubtree():
    def prims(nodes_num, edges, start):
        """
            simple burt not 100% optimized, functional approach
            :param nodes_num: nodes number
            :param edges: graph edge
            :param start: start point
            :return:
        """
        edges_dic = [[] for _ in range(nodes_num + 1)]

        for x, y, w in edges:
            edges_dic[x].append((y, w))
            edges_dic[y].append((x, w))

        in_set = set([start])
        out_set = set([x for x in range(1, nodes_num + 1) if x != start])
        min_w = [10**6] * (nodes_num + 1)
        min_w[start] = 0
        while len(in_set) < nodes_num:
            next_min = 10**6
            next_node = 0
            for node in out_set:
                for n, w in edges_dic[node]:
                   if next_min > w and n in in_set:
                       next_min = w
                       next_node = node

            in_set.add(next_node)
            out_set.remove(next_node)
            min_w[next_node] = next_min
        result = min_w[1:]
        return sum(result)

    n = 5
    edges = [[1, 2, 3], [1, 3, 4], [4, 2, 6], [5, 2, 2], [2, 3, 5], [3, 5, 7]]
    start = 1
    print(prims(n, edges, start))

##################################################################################
# https://www.hackerrank.com/challenges/journey-to-the-moon/problem
# Journey to the Moon


def _journeyToMoon(n, astronaut):
    result = 0
    all_links = [set([i]) for i in range(n)]
    all_dick = set(i for i in range(n))
    for i, val in enumerate(astronaut):
        left_val, right_val = val
        set_big, set_small, small_val = (all_links[right_val], all_links[left_val], left_val) \
            if len(all_links[right_val]) > len(all_links[left_val]) \
            else (all_links[left_val], all_links[right_val], right_val)

        set_big.update(set_small)
        for val in set_small:
            all_links[val] = set_big
            if val in all_dick:
                all_dick.remove(val)

    if len(all_dick) > 1:
        len_ar = [len(all_links[val]) for val in all_dick]
        sum = 0;
        result = 0

        for size in len_ar:
            result += sum * size
            sum += size

        return result


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


def journeyToMoon(n, astronaut):

    all_links = [DisjointSet() for _ in range(n)]
    for i, val in enumerate(astronaut):
        left_val, right_val = val
        left_set = all_links[left_val]
        right_set = all_links[right_val]
        if left_set.size > left_set.size:
            left_set.union(right_set)
        else:
            right_set.union(left_set)

    root_dic = {}
    for set_val in all_links:
        if set_val.parent not in root_dic:
            root_dic[set_val.parent] = set_val.size
        else:
            root_dic[set_val.parent] = max(set_val.size, root_dic[set_val.parent])

    result = 0
    if len(root_dic) > 1:

        len_ar = [val.size for val in root_dic]
        for i in range(len(len_ar) - 1):
            next_val = 0
            for j in range(i + 1, len(len_ar)):
                next_val += len_ar[i] * len_ar[j]
            result += next_val

    return result

#
# case_1 = [[0, 1],
#           [2, 3],
#           [0, 4]]
# print(journeyToMoon(5, case_1))  # 6
#
# case_2 = [[1, 2],
#           [2, 3]]
# print(journeyToMoon(4, case_2))  # 3

##################################################################################