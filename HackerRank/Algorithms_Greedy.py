# Algorithms - Greedy

##################################################################################
# https://www.hackerrank.com/challenges/pylons/problem
# Goodland Electricity


def pylons(plant_range, cities_ar):
    plant_range -= 1
    result = 0
    start = 0
    prev = -1
    while start < len(cities_ar):
        next_step = min(start + plant_range, len(cities_ar) - 1)
        while cities_ar[next_step] != 1 and next_step >= prev:
            next_step -= 1
        if next_step == prev:
            return -1
        result += 1
        start = next_step + plant_range + 1
        prev = next_step
    return result

print(pylons(3, [0, 1, 1, 1, 0, 0, 0]))  # -1
print(pylons(2, [0, 1, 1, 1, 1, 0]))  # 2

##################################################################################

