from Companies.util_decorators import timeit
import math


@timeit
def solution_b(max_sum):
    if max_sum < 12:
        return -1
    max_sum_2 = max_sum / 2
    max_range = int(max_sum / 2.5) + 1 # int(math.sqrt(max_sum)) + 1
    result_ar = [(a, b) for a in range(1, max_range) for b in range(a + 1, max_range) \
                 #if a*a + b*b == (max_sum - a - b) **2 \
                 if max_sum_2 - a - b + a*b / max_sum == 0 \
                 ]
    # result_ar = [(a, b) for a in range(1, max_range) for b in range(1, max_range) if check_pear(a, b, max_sum)]
    result = -1
    if len(result_ar) > 0:
        final_calc = [x[0]*x[1]*(max_sum - x[0] - x[1]) for x in result_ar]
        result = max(final_calc)
    return result


def check_pear(a, b, max_sum):
    return a < b and (max_sum / 2 - a - b + a*b / max_sum) == 0

@timeit
def solution(max_sum):
    largest = -1
    for a in range(1, max_sum // 3 + 1):
        b = max_sum * (a - max_sum // 2) // (a - max_sum)
        c = max_sum - a - b
        if a * a + b * b == c * c:
            product = a * b * c
            # Use := in Python 3.8
            if product > largest:
                largest = product
    return largest
    #print(largest)

#max_sum = 1000
# max_sum = 12
# max_sum = 3000
max_sum = 2992 # 946833360
print(solution(max_sum)) # 31875000


# def divisors(n):
#     for divisor in range(1, int(n**0.5) + 1):
#         if n % divisor == 0:
#             yield divisor, n//divisor
#
# pn = dict()
# for r in range(2, 550, 2):
#     st = r*r // 2
#     for s, t in divisors(st):
#         x = (r+s) + (r+t) + (r+s+t)
#         pn[x] = (r+s) * (r+t) * (r+s+t)
#
# print(pn)
