# https://projecteuler.net/problem=2

def solution(max_num):
    sum_fib = 0
    fib_ar = [1, 2]
    cur_fib = 2
    while cur_fib <= max_num:
        if cur_fib % 2 == 0:
            sum_fib += cur_fib
        cur_fib = fib_ar[0] + fib_ar[1]
        fib_ar[0] = fib_ar[1]
        fib_ar[1] = cur_fib

    return sum_fib

# print(solution(4000000))
print(solution(10)) # 10
print(solution(100)) # 44
