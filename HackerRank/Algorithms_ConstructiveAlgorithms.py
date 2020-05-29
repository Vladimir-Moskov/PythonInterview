######################################################################################
# https://www.hackerrank.com/challenges/an-interesting-game-1/problem
# Gaming Array


# O(n^2) solution
def gamingArray_naive(arr):
    result = 0
    end = len(arr) - 1
    while end >= 0:
        i = 0
        max_i = 0
        while i <= end:
            if arr[max_i] < arr[i]:
                max_i = i
            i += 1
        result += 1
        end = max_i - 1

    if result % 2 == 0:
        return "ANDY"
    return "BOB"


# O(n) solution
def gamingArray(arr):
    result = 1
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
            result += 1

    if result % 2 == 0:
        return "ANDY"
    return "BOB"

arr = [2, 3, 5, 4, 1]  # bob
#print(gamingArray(arr))
arr = [5, 2, 6, 3, 4]  # andy
#print(gamingArray(arr))

######################################################################################