# FibFrog
# https://app.codility.com/programmers/lessons/13-fibonacci_numbers/fib_frog/

class FibFrog():
    def __init__(self):
        self.__is_fib = {}
        pass

    def is_fib(self, value):
        if self.__is_fib.get(value, -1) == -1:
            next_val = 0
            prev_val_0 = 0
            prev_val_1 = 1
            while next_val < value:
                next_val = prev_val_0 + prev_val_1
                prev_val_0 = prev_val_1
                prev_val_1 = next_val
            self.__is_fib[value] = next_val == value
        return self.__is_fib[value]

    def solution(self,given_data):
        num_jump = -1
        available_jump = []
        for i in range(0, len(given_data)):
            if given_data[i] == 1:
                available_jump.append(i + 1)
        last_step = len(given_data) + 1
        if self.is_fib(last_step):
            num_jump = 1
        else:
            available_jump.append(last_step)
            available_jump.reverse()
            num_jump = self.max_fib(available_jump, 0)

        return num_jump

    def max_fib(self, steps_ar, num_jump):
        # steps_ar len > 1
        # iterative deepening algorithm - from max to min step
        next_steps = []
        step_index = []
        k = 0
        for k in range(0, len(steps_ar)):
            step = steps_ar[k]
            if self.is_fib(step):
                next_steps.append(step)
                step_index.append(k)
            k += 1

        if len(next_steps) == 0:
            num_jump = -1
        else:
            num_jump += 1
            for j in range(0, len(next_steps), ):
                step = next_steps[j]
                next_check = steps_ar[0:(step_index[j])]
                # the end
                if len(next_check) == 0:
                    break
                else:
                    for k in range(0, len(next_check)):
                        next_check[k] -= step
                count = self.max_fib(next_check, num_jump)
                if count > 0:
                    num_jump = count
                    break

        return num_jump

# test
# fib_ar = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
#           28657, 46368, 75025, 121393, 196418, 317811]
# for num in fib_ar:
#     print(is_fib(num))

A = [0] * 11
A[0] = 0
A[1] = 0
A[2] = 0
A[3] = 1
A[4] = 1
A[5] = 0
A[6] = 1
A[7] = 0
A[8] = 0
A[9] = 0
A[10] = 0

A = [1] * 13

print(FibFrog().solution(A))