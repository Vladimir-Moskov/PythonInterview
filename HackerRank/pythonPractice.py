
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

def histogrammSolution():
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
    # print(timeit.timeit(stmt=test_code, number=100000))

##############################################################
# Arrays
# https://www.hackerrank.com/challenges/np-arrays/problem

def ArraysSolution():
    import numpy

    def arrays(arr):
        # complete this function
        # use numpy.array
        arr1d = numpy.array(arr, float)
        reversed_arr = numpy.flipud(arr1d)
        return reversed_arr

    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)

####################################################################
# https://www.hackerrank.com/challenges/input/problem
# Input()

def InputSolution():
    x, k = list(map(int, input().split()))
    expression = input()
    result = eval(expression) == k
    print(result)

####################################################################
# Decorators 2 - Name Directory
# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem

def Decorators2():
    import operator


    def person_lister(f):
        def inner(people):
            people = sorted(people, key=lambda person: int(person[2]))
            return map(f, people)

        return inner


    @person_lister
    def name_format(person):
        return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


    if __name__ == '__main__':
        people = [input().split() for i in range(int(input()))]
        print(*name_format(people), sep='\n')

###################################################################
# Classes: Dealing with Complex Numbers
# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary,
                       self.real * no.imaginary + self.imaginary * no.real)

    def __truediv__(self, no):
        return Complex((self.real * no.real + self.imaginary * no.imaginary) / (no.real ** 2 + no.imaginary ** 2),
                       (self.imaginary * no.real - self.real * no.imaginary) / (no.real ** 2 + no.imaginary ** 2))

    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

##########################################################################
# Dot and Cross
# https://www.hackerrank.com/challenges/np-dot-and-cross/problem

def DotandCross():
    import numpy


    N = int(input())
    A = []
    B = []
    for _ in range (N):
        A.append(list(map(int , input().rstrip().split())))
    for _ in range (N):
        B.append(list(map(int , input().rstrip().split())))

    A = numpy.array(A)
    B = numpy.array(B)

    print(numpy.matmul(A, B))

############################################################################
# Inner and Outer
# https://www.hackerrank.com/challenges/np-inner-and-outer/problem

def InnerOuter():
    import numpy

    A = list(map(int , input().rstrip().split()))
    B= list(map(int , input().rstrip().split()))

    A = numpy.array(A)
    B = numpy.array(B)
    print(numpy.inner(A, B))
    print(numpy.outer(A, B))

############################################################################
# Map and Lambda Function
# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

def LambdaFunction():
    cube = lambda x: x**3# complete the lambda function

    def fibonacci(n):
        result = [0] * n

        for i in range(n):
            if i < 2:
              result[i] = i
            else:
                result[i] = result[i-1] + result[i-2]
        return result


    if __name__ == '__main__':
        n = int(input())
        print(list(map(cube, fibonacci(n))))

############################################################################
# ginortS
# https://www.hackerrank.com/challenges/ginorts/problem


def ginortS():
    input_str = input()

    def comparator(ch: str):
        if ch.isupper():
            return ord(ch)
        elif ch.isdigit():
            if int(ch) % 2 == 0:
                 return 66 + ord(ch)
            else:
                return 60 + ord(ch)
        return ord(ch) - 48

    input_str = "".join(sorted(input_str, key=comparator))

    print(input_str)

############################################################################
# https://www.hackerrank.com/challenges/reduce-function/problem
# Reduce Function

def ReduceFunction():
    from fractions import Fraction
    from functools import reduce

    def product(fracs):
        t = reduce(lambda x, y : x * y, fracs)
        return t.numerator, t.denominator

    if __name__ == '__main__':
        fracs = []
        for _ in range(int(input())):
            fracs.append(Fraction(*map(int, input().split())))
        result = product(fracs)
        print(*result)

############################################################################
# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
# Validating Email Addresses With a Filter

def ValidatingEmail():
    def fun(email):
        try:
            username, url = email.split("@")
            website, extension = url.split(".")
        except ValueError:
            return False

        if not username.replace("-", "").replace("_", "").isalnum():
            return False
        if not website.isalnum():
            return False
        if len(extension) > 3:
            return False
        return True


    def filter_mail(emails):
        return list(filter(fun, emails))


    if __name__ == '__main__':
        n = int(input())
        emails = []
        for _ in range(n):
            emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)

############################################################################
# Linear Algebra

def LinearAlgebra():
    import numpy

    N = int(input())
    A = [0] * N
    for i in range(N):
        A[i] = list(map(float, input().split()))

    A = numpy.array(A)
    print(round(numpy.linalg.det(A), 2))

############################################################################
# Polynomials

def Polynomials():
    import numpy
    A = list(map(float, input().split()))
    x = float(input())
    A = numpy.array(A)
    print(numpy.polyval(A, x))

############################################################################
# Standardize Mobile Number Using Decorators

def StandardizeMobile():
    pref = '+91 '
    def wrapper(f):
        def fun(l):
            new_l = []
            for phone in l:
                if phone[0] == '0':
                   phone = pref + phone[1:6] + ' ' + phone[6:]
                elif phone[0] == '+':
                   phone = pref + phone[3:8] + ' ' + phone[8:]
                else:
                   if len(phone) == 10:
                        phone = pref + phone[0:5] + ' ' + phone[5:]
                   else:
                        phone = pref + phone[2:7] + ' ' + phone[7:]
                new_l.append(phone)
            return f(new_l)
        return fun

    @wrapper
    def sort_phone(l):
        print(*sorted(l), sep='\n')

    if __name__ == '__main__':
        l = [input() for _ in range(int(input()))]
        sort_phone(l)


############################################################################
# https://www.hackerrank.com/challenges/incorrect-regex/problem
#

def incorrect_regex():
    import re
    N = int(input())

    for _ in range(N):
        try:
            val = input()
            p = re.compile(val)
            print(True)
        except Exception:
            print(False)

############################################################################
# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem

def XML1solution():
    import sys
    import xml.etree.ElementTree as etree

    def get_attr_number(node):
        result = 0
        result = get_attr_number_recursive(node)
        return result

    def get_attr_number_recursive(node):
        result = len(node.attrib)
        for child in node:
            result += get_attr_number_recursive(child)
        return result

    if __name__ == '__main__':
        sys.stdin.readline()
        xml = sys.stdin.read()
        tree = etree.ElementTree(etree.fromstring(xml))
        root = tree.getroot()
        print(get_attr_number(root))

############################################################################
import xml.etree.ElementTree as etree

def XML2solution():
    maxdepth = 0
    def depth(elem, level):
        global maxdepth
        # your code goes here
        level += 1
        for child in elem:
            next_level = depth(child, level)
            maxdepth = max(maxdepth, next_level)

        return level

    xml = """
    <feed xml:lang='en'>
    
      <title>HackerRank</title>
    
      <subtitle lang='en'>Programming challenges</subtitle>
    
      <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    
      <updated>2013-12-25T12:00:00</updated>
    
      <entry>
    
        <author gender='male'>Harsh</author>
    
        <question type='hard'>XML 1</question>
    
        <description type='text'>This is related to XML parsing</description>
    
      </entry>
    
    </feed>
    """
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


######################################################################
# https://www.hackerrank.com/challenges/simple-text-editor/problem
# Simple Text Editor

def SimpleTextEditor():

    from collections import deque
    # comands_ar = [(comand, str)]

    def runCommands(comands_ar):
        comands_deq = deque()
        current_str = ''
        for comand, *str_val in comands_ar:
            str_val = str_val[0] if str_val else None
            if comand == "1":
                comands_deq.append(current_str)
                current_str += str_val
            elif comand == "2":
                comands_deq.append(current_str)
                val_int = min(int(str_val), len(current_str))
                current_str = current_str[: -val_int]
            elif comand == "3":
                val_int = int(str_val) - 1
                print(current_str[val_int])
            elif comand == "4":
                val = comands_deq.pop()
                current_str = val

    comands_ar = [
    ["1", "ewcgpjfh"],
    ["1", "igqsbqyp"],
    ["1", "qsdliigcj"],
    ["4"],
    ["3", "15"],
    ["1", "iilmgp"],
    ["2", "8"],
    ["4"],
    ["2", "18"],
    ["1", "scwhors"]]

    runCommands(comands_ar)

######################################################################
#
#
