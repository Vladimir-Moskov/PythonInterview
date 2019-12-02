#################### Lesson 10 - 4 #########################

"""

https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/flags/

A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbours. More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

For example, the following array A:
    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2

has exactly four peaks: elements 1, 3, 5 and 10.

You are going on a trip to a range of mountains whose relative heights are represented by array A, as shown in a figure below. You have to choose how many flags you should take with you. The goal is to set the maximum number of flags on the peaks, according to certain rules.

Flags can only be set on peaks. What's more, if you take K flags, then the distance between any two flags should be greater than or equal to K. The distance between indices P and Q is the absolute value |P − Q|.

For example, given the mountain range represented by array A, above, with N = 12, if you take:

        two flags, you can set them on peaks 1 and 5;
        three flags, you can set them on peaks 1, 5 and 10;
        four flags, you can set only three flags, on peaks 1, 5 and 10.

You can therefore set a maximum of three flags in this case.

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the maximum number of flags that can be set on the peaks of the array.

For example, the following array A:
    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2

the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..400,000];
        each element of array A is an integer within the range [0..1,000,000,000].


"""
# total = 86%, correct - 100%, performance = 71%% (brute force)
# and now 100%
class Flags:

    @staticmethod
    def solution(given_points):
        from math import sqrt
        # flags = []
        flag_counter = 0
        distance = []
        points_num = len(given_points)
        if points_num < 2:
            return 0
        index = 1
        prev_index = 0
        # ts = time.time()
        while index < points_num - 1:
            if given_points[index] > given_points[index - 1] and \
               given_points[index] > given_points[index + 1]:
                # flags.append(index)
                flag_counter += 1
                if flag_counter > 1:
                    # distance.append(flags[flag_counter - 1] - flags[flag_counter - 2])
                    distance.append(index - prev_index)
                prev_index = index
                index += 2
            else:
                index += 1

        # print(time.time() - ts)
        # case for only 0, 1 or, 2 peaks
        if flag_counter < 3:
            return flag_counter

        max_flags = 2
        end_flag = int(sqrt(points_num)) + 2
        if flag_counter < end_flag:
            end_flag = flag_counter
        # i = 3
        # for i in range(3, end_flag):
        # for i in range(3, flag_counter):
        i = 3
        if not Flags.can_fit(distance, end_flag):
            while i < end_flag - 1:
                next_f = int(i + end_flag) // 2
                if Flags.can_fit(distance, next_f):
                    i = next_f
                else:
                    end_flag = next_f
            end_flag = i

        # print(time.time() - ts)
        return end_flag

    @staticmethod
    def can_fit(distance, flag_count):
        temp_max = 1
        index = 0
        cur_dis = 0
        result = False
        while index < len(distance):
            cur_dis += distance[index]
            if cur_dis >= flag_count:
                cur_dis = 0
                temp_max += 1
                if temp_max == flag_count:
                    result = True
                    break
            index += 1
        return result

    @staticmethod
    def test():
        A = [0] * 16
        A[0] = 1
        A[1] = 5
        A[2] = 3
        A[3] = 4
        A[4] = 3
        A[5] = 4
        A[6] = 1
        A[7] = 2
        A[8] = 3
        A[9] = 4
        A[10] = 6
        A[11] = 2
        A[12] = 2
        A[13] = 2
        A[14] = 6
        A[15] = 2

        A = [2, 4, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2]
        # A = [random.randint(1, 10) for i in range(0, 200000)]
        print(Flags.solution(A))

Flags.test()