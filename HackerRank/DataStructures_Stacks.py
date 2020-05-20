#############################################################################
# https://www.hackerrank.com/challenges/equal-stacks/problem
# Equal Stacks

def equalStacks(h1, h2, h3):
    sum_1 = sum(h1)
    sum_2 = sum(h2)
    sum_3 = sum(h3)
    last_1 = 0
    last_2 = 0
    last_3 = 0

    while not (sum_1 == sum_2 and sum_1 == sum_3):
        if sum_1 >= sum_2 and sum_1 >= sum_3:
            sum_1 -= h1[last_1]
            last_1 += 1
        elif sum_2 >= sum_1 and sum_2 >= sum_3:
            sum_2 -= h2[last_2]
            last_2 += 1
        elif sum_3 >= sum_1 and sum_3 >= sum_1:
            sum_3 -= h3[last_3]
            last_3 += 1

    return sum_1

h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]

h1 = [1, 1, 1, 1, 2]
h2 = [3, 7]
h3 = [1, 3, 1]

print(equalStacks(h1, h2, h3))

#############################################################################
