# https://app.codility.com/c/feedback/CK33MW-Q27/

# Task no. 	Task score  Correctness Performance Aggregated total score
# Task 1 	100%               100%       N/A         92%
# Task 2 	100%               100%       N/A
# Task 3 	75%                80%        66%

###################################################
# task 1

def _solution(A):
    max_result = 1_000_000_000
    result = 0
    if len(A) < 3:
        return result
    k = 0
    for i in range(1, len(A) - 1):
        if A[i + 1] - A[i] == A[i] - A[i - 1]:
            k += 1
        else:
            if k > 0:
                sum_k = sum([j for j in range(1, k + 1)])
                result += sum_k
            k = 0
    if k > 0:
        sum_k = sum([j for j in range(1, k + 1)])
        result += sum_k

    if result > max_result:
        return -1
    return result

case_1 = [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]
case_2 = [1, 3, 5, 7, 9]
# print(solution(case_1))
# print(solution(case_2))

#######################################################

# task 3

from collections import Counter

def solution(A):
    count_val = Counter(A)
    result = 0

    for val in count_val.values():
        if val == 2:
            result += 1
        elif val > 2:
            result += sum([j for j in range(1, val)])

    return result

case_1 = [3, 5, 6, 3, 3, 5] # 3
print(solution(case_1))

#######################################################