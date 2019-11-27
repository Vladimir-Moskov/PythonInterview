#################### Lesson 3 - FrogJmp ############################
"""


A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

    def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:
  X = 10
  Y = 85
  D = 30

the function should return 3, because the frog will be positioned as follows:

        after the first jump, at position 10 + 30 = 40
        after the second jump, at position 10 + 30 + 30 = 70
        after the third jump, at position 10 + 30 + 30 + 30 = 100

Write an efficient algorithm for the following assumptions:

        X, Y and D are integers within the range [1..1,000,000,000];
        X ≤ Y.


"""

# Solution - 100%
# https://app.codility.com/demo/results/trainingQ4WBMP-8YQ/


class FrogJmp:
    @staticmethod
    def solution(start, end, max_step):
        import math
        return math.ceil((end - start) / max_step)

    @staticmethod
    def test():
        X = 10
        Y = 85
        D = 30
        print(FrogJmp.solution(X, Y, D)) # 3


FrogJmp.test()
####################### Lesson 3 - PermMissingElem ##################
"""


An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

    def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        the elements of A are all distinct;
        each element of array A is an integer within the range [1..(N + 1)].


"""
# solution - 100%
# https://app.codility.com/demo/results/trainingEHX2T4-VC5/

class PermMissingElem:
    @staticmethod
    def solution(given_data):
        actual_sum = sum(given_data)
        size = len(given_data) + 1
        expected_sum = size * (1 + size) // 2
        return expected_sum - actual_sum

    @staticmethod
    def test():
        # A = [1, 3, 4, 5]
        A = [2, 3, 1, 5]
        print(PermMissingElem.solution(A))  # 2

PermMissingElem.test()