
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


if __name__ != '__main__':
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

# Enter your code here. Read input from STDIN. Print output to STDOUT
# The Captain's Room
import math
import os
import random
import re
import sys
from collections import Counter


if __name__ != '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    K = int(input())
    rooms = list(map(int , input().rstrip().split()))

    result = 0
    result = Counter(rooms)
    for key, val in result.items():
        if val == 1:
            result = key
            break
    fptr.write(str(result) + '\n')

    fptr.close()

############################################################
# Calendar Module
# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
import os

if __name__ != '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dates = list(map(int, input().rstrip().split()))

    result = calendar.day_name[calendar.weekday(dates[2], dates[0], dates[1])]

    fptr.write(str(result).upper() + '\n')

    fptr.close()

#############################################################
# Zipped
# https://www.hackerrank.com/challenges/zipped/problem
import os

import os

n, x = map(int, input().split())

sheet = []
for _ in range(x):
    sheet.append(map(float, input().split()))

for i in zip(*sheet):
    print(sum(i)/len(i))


N, X = map(int, input()).split()

students = []
for _ in range(X):
    students.append(map(int, input().split()))

students = zip(*students)
for val in students:
    result = sum(val) / X
    print(result + '\n')

#############################################################

