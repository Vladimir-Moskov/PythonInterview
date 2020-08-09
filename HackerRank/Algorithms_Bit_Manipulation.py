# https://www.hackerrank.com/challenges/sansa-and-xor/problem
# Sansa and XOR

def sansaXor(arr):
    result = 0
    prev = [0] * len(arr)
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            prev[j] = prev[j] ^ arr[j]
            result = result ^ prev[j]

    return result

print(sansaXor([3, 4, 5])) # 6