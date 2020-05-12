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
