# https://projecteuler.net/problem=3
import math



def find_max_prime_factor(end_num):
    max_prime_factor = 0
    factors_ar = []
    max_prime_factor = int(math.sqrt(600851475143)) + 1

    for i in range(2, max_prime_factor):
        if end_num % i == 0:
            factors_ar.append(i)
            factors_ar.append(end_num / i)

    factors_ar = list(set(factors_ar))
    factors_ar.sort()
    return max_prime_factor

_end_num = 600851475143
print(find_max_prime_factor(_end_num))

# 775147
#  486847
# 1234169