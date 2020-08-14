################################################################
# https://www.hackerrank.com/challenges/chocolate-in-box/problem
# Chocolate in Box

# def is_even(val):
#     return val % 2 == 0
#
# def amaunt_one(arr):
#     return len([x for x in arr if x == 1])
#
# def chocolateInBox(arr):
#
#     if not is_even(len(arr)):
#         return len(arr)

def chocolateInBox(arr):
    b = 0
    for i in arr:
        b ^= i
    return sum([int(i ^ b < i) for i in arr])

print(chocolateInBox([2, 3]))  # 1
print(chocolateInBox([2, 3, 3]))  # 3
print(chocolateInBox([3, 3]))  # 0

################################################################