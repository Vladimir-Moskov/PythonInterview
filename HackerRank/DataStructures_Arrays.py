# https://www.hackerrank.com/challenges/arrays-ds/problem
# Arrays - DS


def solutionArraysDS():
    def reverseArray(a):
        mid = int(len(a) / 2)
        for i in range(mid):
            a[i], a[-(i + 1)] = a[-(i + 1)], a[i]
        return a

    print(reverseArray([2, 3, 4, 1]))

########################################################################################3
# https://www.hackerrank.com/challenges/array-left-rotation/problem
# Left Rotation

def solution(given_array, num_shifts):
    if len(given_array) < 2 or num_shifts == 0:
        return given_array
    result_ar = [0] * len(given_array)
    real_shift = num_shifts % len(given_array)
    for i in range(0, real_shift):
        result_ar[- (real_shift - i)] = given_array[i]
    for i in range(real_shift, len(given_array)):
        result_ar[i - real_shift] = given_array[i]
    print(" ".join(map(str, result_ar)))
    return result_ar

# solution([1, 2, 3, 4, 5], 4)

#####################################################################
# https://www.hackerrank.com/challenges/dynamic-array/problem
# Dynamic Array

def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    result = []
    last = 0
    for i, x, y in queries:
        index = (x ^ last) % n
        if i == 1:
            arr[index].append(y)
        else:
            second_index = y % len(arr[index])
            last = arr[index][second_index]
            result.append(last)

    return result

n = 2
queries = [
    [1, 0, 5],
    [1, 1, 7],
    [1, 0, 3],
    [2, 1, 0],
    [2, 1, 1],
]
print(dynamicArray(n, queries))

#####################################################################