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

