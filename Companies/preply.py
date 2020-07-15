

from collections import deque


class Node:
    def __init__(self, value, is_minus, minus_count, parent=None):
        self.value = value
        self.is_minus = is_minus
        self.minus_count = minus_count
        self.parent = parent

    def get_expression(self):
        result = []
        current = self
        while current.parent:
            result.append("-" if current.is_minus else "+")
            current = current.parent
        return "".join(reversed(result))


def PlusMinus(num_int):
    # code goes here
    # time complexity 2 ** (n - 1) :(
    # cant use this terrible online IDE - so copy/past from my development tool
    if num_int < 10:
        return "not possible"

    values = []
    while num_int > 0:
        values.append(num_int % 10)
        num_int = num_int // 10
    values.reverse()
    max_total = sum(num_int)

    current_q = deque([Node(values[0], False, 0)])
    for i in range(1, len(values)):
        new_q = deque()
        for node in current_q:

            left = Node(node.value - values[i], True, node.minus_count + 1, node)
            right = Node(node.value + values[i], False, node.minus_count, node)
            #if left.value > -max_total - left.value
            new_q.append(left)
            #if right.value < max_total - right.value
            new_q.append(right)
            node.left = left
            node.right = right

        current_q = new_q

    current_node = None
    max_minus = 0

    for node in current_q:
        if node.value == 0:
            if max_minus < node.minus_count:
                current_node = node
                max_minus = node.minus_count

    return "not possible" if not current_node else current_node.get_expression()


# print(PlusMinus(199)) # not
# print(PlusMinus(35132)) # "-++-"
# print(PlusMinus(26712)) # "-+--"

from bisect import bisect_left, bisect_right


def LongestIncreasingSequence(arr):
    # time complexity n * logn :(
    # cant use this terrible online IDE - so copy/past from my development tool
    results = [0] * len(arr)
    current_len = 0
    for val in arr:
        current_ind = bisect_left(results, val, 0, current_len)
        if current_ind < 0:
            current_ind = -(current_ind + 1)
        results[current_ind] = val
        if current_ind == current_len:
            current_len += 1
    return current_len

def _LongestIncreasingSequence(arr):
    # time complexity n * 2 :( - can be n * logn with binary search
    # cant use this terrible online IDE - so copy/past from my development toolp
    if len(arr) == 0:
        return 0

    pre_calc_values = [0] * len(arr)
    pre_calc_values[0] = 1
    result = 1
    for i in range(1, len(arr)):
        current_max = 0
        for j in range(i):
            if arr[i] > arr[j]:
                current_max = max(current_max, pre_calc_values[j])
        pre_calc_values[i] = current_max + 1
        result = max(pre_calc_values[i], result)

    return result


print(LongestIncreasingSequence([9, 9, 4, 2]))
print(LongestIncreasingSequence([10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90]))