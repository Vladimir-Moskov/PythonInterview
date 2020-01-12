# https://projecteuler.net/problem=1
# https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem


def solution(max_num):
    max_num -= 1
    div_3 = max_num // 3
    s_3 = div_3 * (3 + div_3 * 3) // 2  # 166833
    div_5 = max_num // 5
    s_5 = div_5 * (5 + div_5 * 5) // 2  # 95550
    div_3_5 = max_num // 15
    s_3_5 = div_3_5 * (15 + div_3_5 * 15) // 2  # 233168.0
    result = s_3 + s_5 - s_3_5
    return int(result)

print(solution(1000))
print(solution(1))
