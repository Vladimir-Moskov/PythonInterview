

############ Lesson 6 - 4 ###############################################

"""
https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/



We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:
  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

There are eleven (unordered) pairs of discs that intersect, namely:

        discs 1 and 4 intersect, and both intersect with all the other discs;
        disc 2 also intersects with discs 0 and 3.

Write a function:

    def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [0..2,147,483,647].



"""


class NumberOfDiscIntersections:
    # brute force for now - 56%, performance = 12
    @staticmethod
    def solution_bad(given_array):
        result = 0
        last_index = len(given_array)
        start_end_point = [[]] * last_index
        for j in range(0, last_index):
            radius = given_array[j]
            start_end_point[j] = [(j - radius), (j + radius)]
        for index in range(0, last_index - 1):
            circle = start_end_point[index]
            for i in range(index + 1, last_index):
                next_c = start_end_point[i]
                if circle[1] >= next_c[0]:
                    result += 1
        return result

    # now - 62%, performance = 25
    @staticmethod
    def solution_better(given_array):
        result = 0
        last_index = len(given_array)
        start_point = [0] * last_index
        end_point = [0] * last_index
        for j in range(0, last_index):
            radius = given_array[j]
            start_point[j] = j - radius
            end_point[j] = j + radius

        start_point.sort()
        end_point.sort()
        for index in range(0, last_index - 1):
            end = end_point[index]
            k = index + 1
            start = start_point[k]
            while end >= start:
                result += 1
                k += 1
                if k > last_index - 1:
                    break
                start = start_point[k]

        return result

    # now - 100%, performance = 100%
    # hm, but some how it scores only 50% with performance = 0 ????
    # https://app.codility.com/demo/results/trainingDQX57W-PZY/
    @staticmethod
    def solution(A):
        events = []
        for i, a in enumerate(A):
            events += [(i - a, +1), (i + a, -1)]
            events.sort(key=lambda x: (x[0], -x[1]))
        intersections, active_circles = 0, 0
        for _, circle_count_delta in events:
            intersections += active_circles * (circle_count_delta > 0)
            active_circles += circle_count_delta
            if intersections > 10E6:
                return -1
        return intersections

    @staticmethod
    def test():
        A = [0] * 6
        A[0] = 1
        A[1] = 5
        A[2] = 2
        A[3] = 1
        A[4] = 4
        A[5] = 0
        print(NumberOfDiscIntersections.solution_bad(A))  # 11
        print(NumberOfDiscIntersections.solution_better(A))  # 11
        print(NumberOfDiscIntersections.solution(A))  # 11


NumberOfDiscIntersections.test()

