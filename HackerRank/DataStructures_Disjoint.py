###################################################################
# https://www.hackerrank.com/challenges/maximum-cost-queries/problem
# Super Maximum Cost Queries

def Super_Maximum_Cost_Queries():
    def solve_(tree, queries):
        from collections import deque
        result = [0] * len(queries)
        edges_dic = [[] for _ in range(len(tree) + 2)]

        for x, y, w in tree:
            edges_dic[x].append((y, w))
            edges_dic[y].append((x, w))
        i = 0
        for min_w, max_w in queries:
            current_result = 0
            for node in range(1, len(edges_dic)):
                set_in = set([node])
                tree_dq = deque([(node, 0)])
                total_w = 0
                while tree_dq:
                    current_node, cur_w = tree_dq.popleft()
                    total_w += cur_w
                    for x, w in edges_dic[current_node]:
                        if total_w + w <= max_w and x not in set_in:
                            set_in.add(x)
                            tree_dq.append((x, total_w + w))
                            if total_w + w >= min_w:
                                current_result += 1

            result[i] = current_result
            i += 1
        return result


    class Node:

        def __init__(self, value, weight=0):
            self.value = value
            self.weight = weight
            self.children = []
            self.connection = []

    def solve(tree, queries):
        from collections import defaultdict, deque
        result = [0] * len(queries)
        edges_dic = [[] for _ in range(len(tree) + 2)]

        for x, y, w in tree:
            edges_dic[x].append((y, w))
            edges_dic[y].append((x, w))

        # build tree
        tree_node_dic = {1: Node(1)}
        tree_dq = deque([1])
        while tree_dq:
            next_q = deque()
            for node in tree_dq:
                children = edges_dic[node]
                for x, w in children:
                    if x not in tree_node_dic:
                        tree_node_dic[x] = Node(x, w)
                        tree_node_dic[node].children.append(tree_node_dic[x])
                        next_q.append(x)
            tree_dq = next_q
        i = 0
        for min_w, max_w in queries:
            current_result = 0
            for n in range(1, len(edges_dic)):
                root = tree_node_dic[n]
                for child in root.children:
                    current_result += path_recursive(child, min_w, max_w, 0)
            result[i] = current_result
            i += 1

        return result

    def path_recursive(node, min_w, max_w, total_max):
        result = 0
        total_max = max(total_max, node.weight)
        if total_max <= max_w and total_max >= min_w:
            result += 1
            for child in node.children:
                result += path_recursive(child, min_w, max_w, total_max)
        return result

    # 1 - 4 - 3
    #   \ 2 -5
    tree = [[1, 2, 3], [1, 4, 2], [2, 5, 6], [3, 4, 1]]
    queries = [[1, 1], [1, 2], [2, 3], [2, 5], [1, 6]]
    # [1, 3, 5, 5, 10]
    print(solve(tree, queries))

    from bisect import bisect_left,bisect_right
    parents = {}
    rep = {}

    def make_set(n):
        global parents, rep
        parents = dict(zip(range(1, n+1), range(1, n+1)))
        rep = dict(zip(range(1, n+1), ({i} for i in range(1, n+1))))

    def add_edge(x, y,paths,w):
        xroot = find(x)
        yroot = find(y)
        paths[w] += len(rep[xroot])*len(rep[yroot])
        if xroot == yroot:
            return
        else:
            if len(rep[yroot]) < len(rep[xroot]):
                parents[yroot] = xroot
                rep[xroot].update(rep[yroot])
                del rep[yroot]
            else:
                parents[xroot] = yroot
                rep[yroot].update(rep[xroot])
                del rep[xroot]

    def find(x):
        if parents[x] != x:
            parent = find(parents[x])
            parents[x] = parent
        return parents[x]

    def solve(tree, queries):
        n = len(tree) + 1
        tree.sort(key=lambda e: e[2])
        paths = {0: 0}
        weights = [0]
        prev = 0
        make_set(len(tree)+1)
        for a, b, w in tree:
            if w != prev:
                weights.append(w)
                paths[w] = paths[prev]
            add_edge(a, b, paths, w)
            prev = w
        for l, r in queries:
            wr = weights[bisect_right(weights, r)-1]
            wl = weights[bisect_right(weights, l-1)-1]
            yield paths[wr]-paths[wl]

###################################################################
# https://www.hackerrank.com/challenges/kundu-and-tree/problem
# Kundu and Tree


class Node:

    def __init__(self, data):
        self.data = data
        self.childs = {}
        self.edge = {}
        self.num_red_path = 0
        self.level = 0

    def add_child(self, child, color):
        self.childs[child.data] = child
        self.edge[child.data] = color

    def calc_r_path(self):
        for child in self.childs.values():
            child.level = self.level + 1
            child.num_red_path = self.num_red_path
            if self.edge[child.data] == "r":
                child.num_red_path += 1
            child.calc_r_path()


def solve(n, tree):
    result = 0

    all_nodes = [Node(x) for x in range(1, n + 1)]
    all_nodes.insert(0, None)
    for val in tree:
        par_v, child_v, color = val
        parent = all_nodes[par_v]
        child = all_nodes[child_v]
        parent.add_child(child, color)

    root = all_nodes[1]
    root.calc_r_path()

    return result


n = 5
tree = [[1, 2, 'b'], [2, 3, 'r'], [3, 4, 'r'], [4, 5, 'b']]
print(solve(n, tree))

# import os
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     tree = []
#
#     for _ in range(n-1):
#         raw_inpit = input().rstrip().split()
#         tree.append([int(raw_inpit[0]), int(raw_inpit[1]), raw_inpit[2]])
#
#
#     result = solve(n, tree)
#
#     fptr.write(str(result))
#     fptr.write('\n')
#
#     fptr.close()


from decimal import Decimal


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


def nc2(n):
    if n < 2:
        return 0
    return Decimal(n*(n-1)/2)


def nc3(n):
    if n < 3:
        return 0
    return Decimal(n*(n-1)*(n-2)/6)


n = int(input())
components = [None]*n
for i in range(n-1):
    a, b, c = input().split()
    a = int(a)-1
    b = int(b)-1
    if c == 'r':
        continue
    if not components[a]:
        components[a] = DisjointSet()
    if not components[b]:
        components[b] = DisjointSet()
    components[a].union(components[b])

uniqueComponents = set()
for x in components:
    if x:
        uniqueComponents.add(x.findParent())
valid_triplets = Decimal(nc3(n))

for x in uniqueComponents:
    valid_triplets -= nc3(x.size)
    valid_triplets -= nc2(x.size)*(n-x.size)
print(int(valid_triplets) % (10**9+7))
