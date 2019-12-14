# https://projecteuler.net/problem=6
# https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem

def solution(end_num):
    result = arichmetic_progression(end_num)
    result = result * result - sum_of_natural_squears(end_num)
    return int(result)

def arichmetic_progression(end_num):
    result = end_num * (1 + end_num) / 2
    return result

def sum_of_natural_squears(end_num):
    result = end_num ** 3 / 3 + end_num * end_num / 2 + end_num / 6
    return result

print(solution(100))