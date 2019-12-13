# https://projecteuler.net/problem=4
# https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem
import math

def solution(max_value):
    result = 0
    palindrome_ar = []
    max_1 = 999
    max_2 = 999
    max_val = min(max_1 * max_2, max_value)
    last_pol = 0
    cur_pol = 0
    # max_val = math.sqrt(max_val)
    # max_1 = int(math.sqrt(max_val)) + 1
    # max_2 = max_1
    for i in range(max_1, 0, -1):
        for j in range(max_1, i, -1):
            cur_val = i * j
            if cur_val < max_val:
                if palindrome(cur_val):
                    #last_pol = cur_val
                    #palindrome_ar.append(cur_val)
                    result = max(result, cur_val)
                    break
                if cur_val <= result:
                    break
            #elif result > 0:
            #    break
        # if last_pol < cur_pol:
        #     break
        # else:
        #     cur_pol = last_pol
    # result = cur_pol
    # result = max(palindrome_ar)
    return result


def palindrome(num):
    return str(num) == str(num)[::-1]


# 9009 91 x 99

# 101110 143 x 707
print(solution(800000)) # 793397
# print(solution(9999999)) # 906609

def solution_2(max_val):
    min_plier = 10 ** (3 - 1)  # Minimum n-digit number for eg. if digits = 3, min_plier = 100
    max_plier = 10 ** 3 - 1    # Maximum n-digit number for eg. if digits = 3, max_plier = 999

    max_palindrome = 0

    for z in range(max_plier, min_plier, -2):
        if z * z < max_palindrome:
            break

        for x in range(max_plier, int((z * z) ** 0.5), -2):
            product = z * x
            #if product <= max_val:
            # Check if product is greater than previously obtained palindrome.
            if product < max_palindrome:
                break
            #if product <= max_val:
            sproduct = str(product)

            # Check if product obtained is palindrome.
            if sproduct == sproduct[::-1]:
                max_palindrome = product
    return max_palindrome