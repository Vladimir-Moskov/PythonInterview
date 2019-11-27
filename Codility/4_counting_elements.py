########## Lesson 4 - MissingInteger ##############


"""


This is a demo task.

Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].



"""
# solution - 100%
# https://app.codility.com/demo/results/trainingTBGCZK-3JQ/


class MissingInteger:
    @staticmethod
    def solution(int_array):
        dic_helper = {}
        num_positive = 1

        for i in int_array:
            if i > 0:
                num_positive += 1
                dic_helper[i] = 1

        for j in range(1, num_positive + 1):
            if dic_helper.get(j, 0) == 0:
                return j

        return 1

    @staticmethod
    def test():
        A = [1, 3, 6, 4, 1, 2]
        A = [1, 2, 3]
        print(MissingInteger.solution(A))  # 5


MissingInteger.test()
