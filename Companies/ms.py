
# def is_palindrom(str_value: str):
#     result = True
#     mid = int(len(str_value) / 2)
#     v = reversed(str_value[mid::-])
#     return str_value[:mid] == v
#
#     # for i in range(mid):
#     #     if not str_value[i] == str_value[-(i + 1)]:
#     #         result = False
#     #         break
#     #
#     # return result
#
#
# print(is_palindrom('12321'))  # True
# print(is_palindrom('1221'))  # True
# print(is_palindrom('123'))  # False


input_val = [(1, 5), (2, 6), (7, 9)]  # -> 7 not 8
input_val = [(1, 10000000000000)]

# left, right = (min, max)
# [(left, right), ()]

# class CalculateLen:
#     def __init__(self, ):


def merge_tupple(left_tup, right_tup):
    x1, x2 = left_tup
    y1, y2 = right_tup
    if y1 <= x1 <= y2:
        return [(y1, max(y2, x2))]
    elif y1 <= x2 <= y2:
        return [(min(y1, x1), y2)]

    return [left_tup, right_tup]


def calculate_len(list_val):
    result = 0

    count_dic = set()
    for point in list_val:
        x1, x2 = point
        for i in range(x1, x2 + 1):
            count_dic.add(i)

    result = len(count_dic)

    return result

def calculate_len_2(list_val):
    tuple_lst = []
    for point in list_val:
        merge_tupple

print(calculate_len_2(input_val))