############################################################################

def getChange(amoun, price):
    available = [100, 50, 25, 10, 5, 1]
    change = round((amoun - price) * 100)
    result = [0] * 6
    start = 0

    while change and start < len(available):
        if change >= available[start]:
            result[- (start + 1)] = change // available[start]
            change = change % available[start]
        start += 1

    if change > 0:
        return -1

    return result


# should return [1,0,0,0,0,4]

# print(getChange(5, 0.99))
#
# print(getChange(3.14, 1.99)) # // should return [0,1,1,0,0,1]
#
# print(getChange(3, 0.01)) # // should return [4,0,2,1,1,2]
#
# print(getChange(4, 3.14)) # // should return [1,0,1,1,1,0]
#
# print(getChange(0.45, 0.34)) # // should return [1,0,1,0,0,0]



############################################################################


def minesweeper(given_matrix):
    mine = "X"
    delta = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 0), (1, -1), (1, 1)]
    row = len(given_matrix)
    col = len(given_matrix[0])
    result = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if given_matrix[i][j] != mine:
                for x, y in delta:
                    cel_x = i + x
                    cel_y = j + y
                    if cel_x >= 0 and cel_x < row and cel_y >= 0 and cel_y < col:
                        if given_matrix[cel_x][cel_y] == mine:
                            result[i][j] += 1

            else:
                result[i][j] = mine

    return result

test_val_1 = ["XOO", "OOO", "XXO"]



test_val_1 = ["XOOXXXOO", "OOOOXOXX", "XXOXXOOO", "OXOOOXXX", "OOXXXXOX", "XOXXXOXO", "OOOXOXOX", "XOXXOXOX"]

test_val_1 = ["OOOXXXOXX", "XXXXXXOXX", "XOOXXXXXX", "OOXXOXOXX", "XXXXXXXXX"]



# 2 3 4 X X X 4 X X
#
# X X X X X X 7 X X
#
# X 5 6 X X X X X X
#
# 3 5 X X 8 X 8 X X
#
# X X X X X X X X X

result = minesweeper(test_val_1)
for val in result:
    print(val)


# X 1 1 X X X 3 2
#
# 3 3 3 5 X 5 X X
#
# X X 3 X X 5 5 4
#
# 3 X 5 5 6 X X X
#
# 2 4 X X X X 6 X
#
# X 3 X X X 5 X 3
#
# 2 4 5 X 6 X 5 X
#
# X 2 X X 4 X 4 X










