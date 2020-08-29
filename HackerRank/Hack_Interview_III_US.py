
# Hack the Interview III
# https://www.hackerrank.com/contests/hacktheinterview3/challenges

#########################################################################################
# https://www.hackerrank.com/contests/hacktheinterview3/challenges/distribution-in-m-bins
# Product Distribution

def maxScore(a, m):
    result = 0
    if m >= len(a):
        return sum(a) % 1000000007
    a.sort()
    k = 1
    j = 0
    for i, val in enumerate(a):
        if i + m <= len(a):
            if j == m:
                j = 0
                k += 1
            j += 1
        result = (result + k * val) % 1000000007

    return result




# case 0 - 27
a = [1, 5, 4, 2, 3]
m = 2
# print(maxScore(a, m))

# case 1 - 21
a = [4, 1, 9, 7]
m = 4
# print(maxScore(a, m))

#########################################################################################
# https://www.hackerrank.com/contests/hacktheinterview3/challenges/maximal-char-requests
# Maximal Char Requests

