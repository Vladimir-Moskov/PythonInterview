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

#########################################################################
# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
# Hackerland Radio Transmitters


def hackerlandRadioTransmitters_to_complecated(sity_map, trans_range):
    result = 0

    if len(sity_map) < 2:
        return 1
    sity_map.sort()
    left = 0
    next = 1
    while next < len(sity_map):
        first = sity_map[next] - sity_map[left]
        if first >= trans_range:
            result += 1
            next = next if first == trans_range else next - 1
            right = next + 1
            while right < len(sity_map):
                second = sity_map[right] - sity_map[next]
                if second >= trans_range:
                    left = right + 1 if second == trans_range else right
                    next = left + 1
                    break
                else:
                    right += 1
            if right >= len(sity_map):
                break
        else:
            next += 1
        if next >= len(sity_map):
            result += 1

    return result

def hackerlandRadioTransmitters(sity_map, trans_range):
    sity_map.sort()
    result = 0
    start = 0

    while start < len(sity_map):
        curent = sity_map[start]
        while start < len(sity_map) and sity_map[start] - curent <= trans_range:
            start += 1

        result += 1  # build a antenna

        curent = sity_map[start - 1]
        while start < len(sity_map) and sity_map[start] - curent <= trans_range:
            start += 1
    return result

# sity_map = [1, 2, 3, 4, 5]  # 2
# trans_range = 1
# print(hackerlandRadioTransmitters(sity_map, trans_range))
# sity_map = [7, 2, 4, 6, 5, 9, 12, 11] # 3
# trans_range = 2
# print(hackerlandRadioTransmitters(sity_map, trans_range))
# sity_map = [9, 5, 4, 2, 6, 15, 12] # 4
# trans_range = 2
# print(hackerlandRadioTransmitters(sity_map, trans_range))

#########################################################################