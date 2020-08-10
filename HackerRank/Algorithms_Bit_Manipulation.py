#############################################################
# https://www.hackerrank.com/challenges/sansa-and-xor/problem
# Sansa and XOR


# DP approach
def sansaXor(arr):
    result = 0
    prev = [0] * len(arr)
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i - 1, -1):
            if i == 0:
                v = prev[j] ^ arr[j]
            else:
                v = prev[j - 1] ^ arr[j]
            prev[j] = v
            result = result ^ prev[j]

    return result


# try bit-master approach
def sansaXor(arr):
    result = arr[0]
    if len(arr) % 2 == 0:
        return 0

    for j in range(2, len(arr), 2):
        result ^= arr[j]

    return result

# print(sansaXor([3, 4, 5])) # 6
# print(sansaXor([3, 4, 5, 6])) #  0

########################################################