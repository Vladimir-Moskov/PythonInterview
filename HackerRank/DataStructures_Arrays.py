# https://www.hackerrank.com/challenges/arrays-ds/problem
# Arrays - DS


def solutionArraysDS():
    def reverseArray(a):
        mid = int(len(a) / 2)
        for i in range(mid):
            a[i], a[-(i + 1)] = a[-(i + 1)], a[i]
        return a

    print(reverseArray([2, 3, 4, 1]))

##########################################
