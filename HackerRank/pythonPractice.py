
########################################################################################
# Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem

import math
import os
import random
import re
import sys
def Mutations():
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

def _counter():
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

def calendar_day_name():
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

def Zipped():
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
#
# Python3 program to find maximum
# rectangular area in linear time

def max_area_histogram(histogram):

    # This function calulates maximum
    # rectangular area under given
    # histogram with n bars

    # Create an empty stack. The stack
    # holds indexes of histogram[] list.
    # The bars stored in the stack are
    # always in increasing order of
    # their heights.
    stack = list()

    max_area = 0 # Initialize max area

    # Run through all bars of
    # given histogram
    index = 0
    while index < len(histogram):

        # If this bar is higher
        # than the bar on top
        # stack, push it to stack

        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1

        # If this bar is lower than top of stack,
        # then calculate area of rectangle with
        # stack top as the smallest (or minimum
        # height) bar.'i' is 'right index' for
        # the top and element before top in stack
        # is 'left index'
        else:
            # pop the top
            top_of_stack = stack.pop()

            # Calculate the area with
            # histogram[top_of_stack] stack
            # as smallest bar
            area = (histogram[top_of_stack] *
                   ((index - stack[-1] - 1)
                   if stack else index))

            # update max area, if needed
            max_area = max(max_area, area)

    # Now pop the remaining bars from
    # stack and calculate area with
    # every popped bar as the smallest bar
    while stack:

        # pop the top
        top_of_stack = stack.pop()

        # Calculate the area with
        # histogram[top_of_stack]
        # stack as smallest bar
        area = (histogram[top_of_stack] *
              ((index - stack[-1] - 1)
                if stack else index))

        # update max area, if needed
        max_area = max(max_area, area)

    # Return maximum area under
    # the given histogram
    return max_area
import timeit
import inspect

# Driver Code
hist = [6, 2, 5, 4, 5, 1, 6]
print("Maximum area is",
       max_area_histogram(hist))

test_code = inspect.getsource(max_area_histogram)
test_code += """
hist = [6, 2, 5, 4, 5, 1, 6]
max_area_histogram(hist)"""
print(timeit.timeit(stmt=test_code, number=100000))



