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

    max_area = 0  # Initialize max area

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


# Driver Code
hist = [6, 2, 5, 4, 5, 1, 6]
# print("Maximum area is",  max_area_histogram(hist))


###########################################################
# Maximum Xor
def maxXor_naiv(arr, queries):
    result = [0] * len(queries)
    arr_set = set(arr)
    temp_result = [0] * len(arr_set)
    for i, q_val in enumerate(queries):
        temp_max = 0
        for j, num_val in enumerate(arr_set):
            temp_result[j] = num_val ^ q_val
        result[i] = max(temp_result)
    return result


def maxXor(arr, queries):
    ans = []
    trie = {}
    k = len(bin(max(arr+queries))) - 2
    for number in ['{:b}'.format(x).zfill(k) for x in arr]:
        node = trie
        for char in number:
            node = node.setdefault(char, {})
    for n in queries:
        node = trie
        s = ''
        for char in'{:b}'.format(n).zfill(k) :
            tmp = str(int(char) ^ 1)
            tmp = tmp if tmp in node else char
            s += tmp
            node = node[tmp]
        ans.append(int(s, 2) ^ n)
    return ans
num_ar = [0, 1, 2]
cases = [3, 7, 2]

num_ar = [5, 1, 7, 4, 3]
cases = [2, 0]

# import time
# te = time.time()
# for _ in range(1000000):
    # x = maxXor(num_ar, cases)
    # print(maxXor(num_ar, cases))
# print(time.time() - te)

###########################################################
# Cycle Detection
# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

def has_cycle(head):
    if not head:
        return 0

    slow = head;
    fast = head;

    while fast and fast.next:
        slow = slow.next;
        fast = fast.next.next;

        if slow == fast:
            return 1;

    return 0;


###########################################################
# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
def findMergeNode(headA, headB):
    curA = headA
    curB = headB
    while not curA == curB:
        if curA.next is None:
            curA = headB
        else:
            curA = curA.next
        if curB.next is None:
            curB = headA
        else:
            curB = curB.next
    return curA.data

###########################################################
# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Count Triplets
import math
from collections import defaultdict

def countTriplets_0(arr, base):
    result = 0
    count_ar = [0] * len(arr)
    for x in arr:
        val = round(math.log(x, base), 4)
        if val == math.floor(val):
            count_ar[int(val)] += 1
    y = 0
    while y < len(count_ar) - 2:
        result += count_ar[y] * count_ar[y + 1] * count_ar[y + 2]
        y += 1
    return result

def countTriplets(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1

    return count

# print(countTriplets([1, 2, 2, 4], 2)) # 2
# print(countTriplets([1, 3, 9, 9, 27, 81], 3)) # 6
# print(countTriplets([1, 5, 5, 25, 125], 5)) # 4

###################################################################
# Inserting a Node Into a Sorted Doubly Linked List
# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists

# class DoublyLinkedListNode:
#      int data
#      DoublyLinkedListNode next
#      DoublyLinkedListNode prev

# def sortedInsert(head, data):
#     node = DoublyLinkedListNode(data)
#     current_node = head
#     while current_node.data < data and current_node.next:
#         current_node = current_node.next
#
#     if current_node.data < data:
#         node.prev = current_node
#         current_node.next = node
#     else:
#         node.prev = current_node.prev
#         node.next = current_node
#         current_node.prev = node
#         if node.prev:
#             node.prev.next = node
#
#     return head if head.data < data else node
#
# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

#######################################################
# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists
# Insert a node at a specific position in a linked list
# def insertNodeAtPosition(head, data, position):
#     new_node = SinglyLinkedListNode(data)
#     if not head:
#         return
#
#     if position == 0:
#         new_node.next = head
#         return new_node
#
#     current_node = head
#     counter = 1
#     while counter < position:
#         current_node = current_node.next
#         counter += 1
#         if not current_node:
#             break;
#     if current_node:
#         new_node.next = current_node.next
#         current_node.next = new_node
#
#     return head

#######################################################