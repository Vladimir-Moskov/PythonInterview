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

import time
te = time.time()
for _ in range(1000000):
    x = maxXor(num_ar, cases)
    # print(maxXor(num_ar, cases))
print(time.time() - te)

