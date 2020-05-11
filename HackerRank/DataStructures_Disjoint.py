###################################################################
# https://www.hackerrank.com/challenges/maximum-cost-queries/problem
# Super Maximum Cost Queries


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


def solve(tree, queries):
    result = [0] * len(queries)

    return result

tree = [[1, 2, 3], [1, 4, 2], [2, 5, 6], [3, 4, 1]]
queries = [[1, 1], [1, 2], [2, 3], [2, 5], [1, 6]]

print(solve(tree, queries))
