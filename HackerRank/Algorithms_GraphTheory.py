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



