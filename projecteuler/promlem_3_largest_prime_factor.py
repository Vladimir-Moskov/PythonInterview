# https://projecteuler.net/problem=3
import math


prime_set = {1, 2, 3, 5, 7, 11, 13, 17}
# not_prime_set = {4, 6, 8, 9}
# not_prime_set = {4, }

def solution(end_num):
    factors_ar = [end_num]
    index = 0
    while index < len(factors_ar):
        index = find_max_prime_factor(factors_ar, index)
    if len(factors_ar) == 0:
        result = 1
    else:
        result = max(factors_ar)
    return result


def find_max_prime_factor(factors_ar, index):
    is_prime = True
    end_num = factors_ar[index]
    if end_num in prime_set:
        index += 1
    # elif end_num in not_prime_set:
    #    factors_ar.remove(end_num)
    else:
        temp_end = int(math.sqrt(end_num)) + 1
        for i in range(2, temp_end, 1):
            if end_num % i == 0:
                is_prime = False
                factors_ar.append(i)
                factors_ar.append(end_num // i)
                break
        if not is_prime:
            # not_prime_set.add(end_num)
            factors_ar.remove(end_num)
        else:
            prime_set.add(end_num)
            index += 1
    return index



_end_num = 600851475143
print(solution(_end_num))
_end_num = 7
print(solution(_end_num))
_end_num = 13195
print(solution(_end_num))
_end_num = 10
print(solution(_end_num))
_end_num = 17
print(solution(_end_num))

# 775147
#  486847
# 1234169