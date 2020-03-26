
########################################################################################
# Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem

import math
import os
import random
import re
import sys

# Set Mutations
def setOperation(operation, A, B):
    #if operation == 'intersection_update':
    func = eval('A.' + operation)
    func(B)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    A = int(input())
    setA = set(map(int , input().rstrip().split()))

    N = int(input())
    for _ in range(N):
        operation = input().rstrip().split()[0]
        B = set(map(int , input().rstrip().split()))

        setOperation(operation, setA, B)

    fptr.write(str(sum(setA)) + '\n')

    fptr.close()
########################################################################################