# Date: 2019-01-24


def numberAmazonTreasureTrucks(rows, column, grid):
    """
        have to do it in my IDE, to slow run/compile time, crazy prompt too annoying

         solution can be optimized, have time limitation for now
    """
    from collections import deque

    valid_cell = 1
    result = 0
    visited_grid = [[0 for _ in range(column)] for _ in range(rows)]
    park_deque = deque()

    for i, row in enumerate(grid):
        for j, cel in enumerate(row):
            if visited_grid[i][j] == 0:
                visited_grid[i][j] = 1
                if cel == valid_cell:
                    result += 1
                    park_deque.append((i, j))
                    while len(park_deque) > 0:
                        cel_i, cel_j = park_deque.popleft()
                        next_i = cel_i + 1
                        next_j = cel_j + 1
                        prev_i = cel_i - 1
                        prev_j = cel_j - 1
                        if next_i < rows and visited_grid[next_i][cel_j] == 0:
                            visited_grid[next_i][cel_j] = 1
                            if grid[next_i][cel_j] == valid_cell:
                                park_deque.append((next_i, cel_j))
                        if next_j < column and visited_grid[cel_i][next_j] == 0:
                            visited_grid[cel_i][next_j] = 1
                            if grid[cel_i][next_j] == valid_cell:
                                park_deque.append((cel_i, next_j))
                        if prev_i > -1 and visited_grid[prev_i][cel_j] == 0:
                            visited_grid[prev_i][cel_j] = 1
                            if grid[prev_i][cel_j] == valid_cell:
                                park_deque.append((prev_i, cel_j))
                        if prev_j > -1 and visited_grid[cel_i][prev_j] == 0:
                            visited_grid[cel_i][prev_j] = 1
                            if grid[cel_i][prev_j] == valid_cell:
                                park_deque.append((cel_i, prev_j))

    return result

case_1 = [[1,1,0,0], [0, 0, 1, 0], [0, 0, 0, 0], [1, 0, 1, 1], [1, 1, 1, 1]]
# print(numberAmazonTreasureTrucks(5, 4, case_1))




def minimumHours(rows, columns, grid):
    """
        have to do it in my IDE, to slow run/compile time, crazy prompt too annoying

         solution can be optimized, have time limitation for now
    """
    result = 0
    empty_server = 0
    calculation_grid = [[0 for _ in range(columns)] for _ in range(rows)]
    def check_all_zeros(i, j):
        if i > 0 and grid[i-1][j] != empty_server:
            return False
        if j > 0 and grid[i][j - 1] != empty_server:
            return False
        if i < columns and grid[i + 1][j] != empty_server:
            return False
        if j < rows and grid[i ][j+1] != empty_server:
            return False
        return True

    def get_min(i, j):
        res = columns*rows
        if i > 0:
            res = min(calculation_grid[i-1][j], res)
        if j > 0:
            res = min(calculation_grid[i][j-1], res)
        return res

    for i, row in enumerate(grid):
        for j, cel in enumerate(row):
            if grid[i][j] == empty_server:
                calculation_grid[i][j] = 1 + get_min(i, j)
                result = max(result, calculation_grid[i][j])
            else:
                calculation_grid[i][j] = 0


    # it suppose to be in corner, cant make it work so far
    # result = calculation_grid[-1][-1]
    return result

case_2 = [[0, 1, 1, 0, 1], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0]]
print(minimumHours(4, 5, case_2))













