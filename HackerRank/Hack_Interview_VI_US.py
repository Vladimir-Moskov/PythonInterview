######################################################################
# https://www.hackerrank.com/contests/hack-the-interview-vi/challenges

######################################################################
# https://www.hackerrank.com/contests/hack-the-interview-vi/challenges/maximum-sum-10-1
# Array-Sum Operation

# 100% solution
def performOperations(N, op):
    result = [0] * len(op)
    ar = [i for i in range(1, N + 1)]
    key_set = set(ar)
    current_sum = sum(ar)
    for i, operation in enumerate(op):
        if operation in key_set:
            ar[0], ar[-1] = ar[-1], ar[0]
        else:
            key_set.remove(ar[-1])
            key_set.add(operation)
            current_sum = current_sum - ar[-1] + operation
            ar[-1] = operation

        result[i] = current_sum

    return result

N = 3
op = [4, 2]
print(performOperations(N, op))

######################################################################