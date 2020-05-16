#########################################################################
# https://www.hackerrank.com/challenges/red-knights-shortest-path/problem
# Red Knight's Shortest Path


def solutionRedKnightShortestPath():
    from collections import deque

    # another old good BFS
    def printShortestPath(n, i_start, j_start, i_end, j_end):
        steps = [("UL", -2, -1), ("UR", -2, 1), ("R", 0, 2), ("LR", 2, 1), ("LL", 2, -1), ("L", 0, -2)]
        path_q = deque([(i_start, j_start)])
        field_matrix = [[0]*n for _ in range(n)]
        field_matrix[i_start][j_start] = 1
        result = 0
        steps_trace = {(i_start, j_start): []}
        while path_q:
            next_q = deque()
            result += 1
            while path_q:
                cur_pos = path_q.popleft()
                x, y = cur_pos
                for step in steps:
                    name, next_pos_x, next_pos_y = step
                    next_pos_x += x
                    next_pos_y += y
                    if next_pos_x == i_end and next_pos_y == j_end:
                        steps_trace[(x, y)].append(name)
                        print(result)
                        print(" ".join(steps_trace[cur_pos]))
                        return result, steps_trace[cur_pos]
                    if 0 <= next_pos_x < n and 0 <= next_pos_y < n:
                        if field_matrix[next_pos_x][next_pos_y] == 0:
                            field_matrix[next_pos_x][next_pos_y] = 1
                            next_q.append((next_pos_x, next_pos_y))
                            steps_trace[(next_pos_x, next_pos_y)] = steps_trace[cur_pos][::]
                            steps_trace[(next_pos_x, next_pos_y)].append(name)
            path_q = next_q
        print("Impossible")
        return -1

    print(printShortestPath(7, 6, 6, 0, 1))  # 4 UL UL UL L
    print(printShortestPath(6, 5, 1, 0, 5))  # Impossible
    print(printShortestPath(7, 0, 3, 4, 3))  # 2 LR LL



