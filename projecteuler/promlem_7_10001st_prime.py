# https://projecteuler.net/problem=7
# https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem

from Companies.util_decorators import timeit

@timeit
def solution(n):
    #nums_ar = list(range(5, 104743 + 2, 2))
    #nums_ar = [x for x in (range(5, 104743 + 2, 2)) if x % 3 != 0 and x % 5 != 0]
    #nums_ar.insert(0, 5)
    primes_ar = [1] * n #[2, 3]
    primes_ar[0] = 2
    primes_ar[1] = 3
    k = 2
    index = 0
    if n == 1:
        return 2
    if n == 2:
        return 3
    max_num = 5
    while k < n:
        # cur_num = nums_ar[index]
        cur_num = max_num
        max_num += 2
        is_prime = 1
        for i in range(1, k//2):
            test_num = primes_ar[i]
            if cur_num % test_num == 0:
                is_prime = 0
                break
        if is_prime:
            # primes_ar.append(cur_num)
            primes_ar[k] = cur_num
            k += 1
        #index += 1

    result = primes_ar[n - 1]
    return result

def solution_b(n):
    nums_ar = [x for x in (range(5, 104743 + 2, 2)) if x % 3 != 0 and x % 5 != 0]

n = 10001 # 104743 - 4596
# n = 168 # 997
# n = 500 # 3571
# n = 6
# n = 3
# n = 6
# n = 10
# print("104743 ->" + str(solution(10001)))
# print("3571 ->" + str(solution(500)))
# print("997 ->" + str(solution(168)))
# print("13 ->" + str(solution(6)))
# print("5 ->" + str(solution(3)))
# print("29 ->" + str(solution(10)))


# def sum_of_natural_squears(end_num):
#     result = end_num ** 3 / 3 + end_num * end_num / 2 + end_num / 6
#     return result

def is_prime(n):
    nums_to_check = range(2, int(n**.5) + 1)
    for i in nums_to_check:
        if n % i == 0:
            return False
    return True

@timeit
def prime_at_index(idx):
    if idx == 1:
        return 2
    if idx == 2:
        return 3
    n_primes = 2
    n = 3
    while n_primes < idx:
        n_primes += 1
        n += 2
        nums_to_check = range(2, int(n ** .5) + 1)
        for i in nums_to_check:
            if n % i == 0:
                n_primes -= 1
                break
        # if is_prime:
        #    n_primes += 1
    return n


p = {i for i in range(2, 105000)}
for i in range(2, 325):
    p = p.difference({i for i in range(i * 2, 200000, i)})
p = list(sorted(p))

for a0 in range(t):
    n = int(input().strip())
    # print(prime_at_index(n))
    # print(primes(n))
    print(p[n - 1])
print(prime_at_index(10001))