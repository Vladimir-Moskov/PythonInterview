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

case_2 = [[0, 1, 1, 0, 1],
          [0, 1, 0, 1, 0],
          [0, 0, 0, 0, 1],
          [0, 1, 0, 0, 0]]
# print(minimumHours(4, 5, case_2))

##############################################

# You are the owner of a coworking space like WeWork and your office building is rectangular. Your team just built wall partitions to create mini offices for startups. This office campus is represented by a 2D array of 1s (floor spaces) and 0s (walls). Each point on this array is a one foot by one foot square. You need to calculate the number of offices. A single office is bordered by walls and is constructed by placing floors next to each other, horizontally and/or vertically. Two 1s adjacent to each other horizontally or vertically are always part of the same office.
#
# Functions
#
# numOffices() has one parameter:
#
#     grid: a 2D grid/array of 1s and 0s
#
#
# Input Format
#
# For some of our templates, we have handled parsing for you. If we do not provide you a parsing function, you will need to parse the input directly. In this problem, our input format is as follows:
#
#     The first line is the number of rows in the 2D array
#     The second line is the number of columns in the 2D array
#     The rest of the input contains the data to be processed
#
# Here is an example of the raw input:
#
# 4
# 5
# 11110
# 11010
# 11000
# 00000
#
#
# Expected Output
#
# Return the number of valid offices in the grid.
#
# Constraints
#
#     Assume all four edges of the grid are all surrounded by walls.
#     Assume that the bounds of the array are the following:
#     The total amount of elements in the array: width x height <= 10^6
#
#
# Example
#
# Example numOffices() Input
#
# grid:
# 	[[1, 1, 0, 0, 0],
# 	 [1, 1, 0, 0, 0],
# 	 [0, 0, 1, 0, 0],
# 	 [0, 0, 0, 1, 1]]
#
# Example Output
#
# 3
#
# Solution
# There's 3 offices in this grid, one made of four 1s on the top left, one made of one 1 in the middle, and one made of two 1s in the bottom right.


class Solution(object):
    def numOffices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        from collections import deque
        column = len(grid[0])
        rows = len(grid)
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


# 3
matrix =[[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1]]

matrix_2 =[[1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0],
         [1, 1, 1, 0, 1]]

sol = Solution()
# print(sol.numOffices(matrix))
# print(sol.numOffices(matrix_2))


################################################################
# You are again the owner of a coworking space like WeWork and your office building is rectangular. You team just created many wall partitions to create mini offices for startups. Your office campus is represented by a 2D array of 1s (floor spaces) and 0s (walls). Each point on this array is a one foot by one foot square. Before renting to tenants, you want to reserve an office for yourself. You wish to fit the largest possible rectangular table in your office, and you will select the office that fits this table. The table sides will always be parallel to the boundaries of the office building. What is the area of the biggest table that can fit in your office?
#
# Functions
#
# biggestTable() has one parameter:
#
#     grid: a 2D grid/array of 1s and 0s
#
#
# Input Format
#
# For some of our templates, we have handled parsing for you. If we do not provide you a parsing function, you will need to parse the input directly. In this problem, our input format is as follows:
#
#     The first line is the number of rows in the 2D array
#     The second line is the number of columns in the 2D array
#     The rest of the input contains the data to be processed
#
# Here is an example of the raw input:
#
# 4
# 5
# 11110
# 11010
# 11000
# 00000
#
#
# Expected Output
#
# Return the area of the biggest right-angled parallelogram made of 1s in the grid. Assume the grid is surrounded by 0s (walls).
#
# Constraints
#
#     Assume that the bounds of the array are the following:
#     The total amount of elements in the array: width x height <= 10^6
#
#
# Example
#
# Example biggestTable() Input
#
# grid:
# 	[[1, 0, 1, 1, 1],
# 	 [1, 0, 1, 1, 1],
# 	 [1, 1, 1, 1, 1],
# 	 [1, 0, 0, 1, 0]]
#
# Example Output
#
# 9
#
# Solution
# The top right of the grid consists of a rectangle with nine 1s in it, the biggest possible space for our table.

class Solution:


    def biggestTable(self, grid):
        row = len(grid)  # no. of rows in M[][]
        column = len(grid[0])  # no. of columns in M[][]

        matrix_helper = [[0 for k in range(column)] for l in range(row)]
        # here we have set the first row and column of S[][]

        # Construct other entries
        for i in range(0, row):
            for j in range(0, column):
                if i ==0 or j == 0:
                    matrix_helper[i][j] = grid[i][j]
                elif (grid[i][j] == 1):
                    matrix_helper[i][j] = min(matrix_helper[i][j - 1], matrix_helper[i - 1][j],
                                  matrix_helper[i - 1][j - 1]) + 1
                else:
                    matrix_helper[i][j] = 0

        # Find the maximum entry and
        # indices of maximum entry in S[][]
        max_of_s = max(map(max, matrix_helper))
        return max_of_s

 # 9
grid = [[1, 0, 1, 1, 1],
	    [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]]
# 6
grid = [[1, 0, 1, 0, 0],
	    [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]]
sol = Solution()
bigTable = sol.biggestTable(grid)

print(bigTable)
