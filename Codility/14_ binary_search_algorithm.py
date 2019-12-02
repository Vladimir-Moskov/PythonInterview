"""

MinMaxDivision

https://app.codility.com/programmers/lessons/14-binary_search_algorithm/min_max_division/


You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.

The large sum is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2

The array can be divided, for example, into the following blocks:

        [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
        [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
        [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
        [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.

The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

Write a function:

    class Solution { public int solution(int K, int M, int[] A); }

that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.

For example, given K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2

the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

        N and K are integers within the range [1..100,000];
        M is an integer within the range [0..10,000];
        each element of array A is an integer within the range [0..M].

[0][0][6]

[0][1][5]
[0][2][4]
[0][3][3]
[0][4][2]
[0][5][1]

"""


class MinMaxDivision:

    # lets start with brute force
    @staticmethod
    def solution(slice_num, max_value, given_data):
        result = 0
        data_len = len(given_data)
        all_slices = []

        first_slice = [0] * slice_num
        first_slice[slice_num - 1] = data_len
        all_slices.append(first_slice)

        for i in range(slice_num - 1, 0, -1):
            cur_len = len(all_slices)
            for j in range(0, cur_len):
                sub_ar = all_slices[j]
                last_el = sub_ar[i]
                prev_el = sub_ar[i - 1]
                for k in range(1, last_el + 1):
                    next_sub_ar = sub_ar[:]
                    prev_el += 1
                    last_el -= 1
                    next_sub_ar[i] = last_el
                    next_sub_ar[i - 1] = prev_el
                    all_slices.append(next_sub_ar)

        result = MinMaxDivision.max_sum_sublist(positions, given_data)

        return result


    @staticmethod
    def solution_0(slice_num, max_value, given_data):
        result = 0
        positions = [0] * slice_num
        size = len(given_data) // slice_num

        for i in range(1, slice_num):
            positions[i - 1] = size * i

        current_max = max_value * slice_num
        result = MinMaxDivision.max_sum_sublist(positions, given_data)

        return result

    @staticmethod
    def max_sum_sublist(positions, int_ar):
        if len(int_ar) == 0:
            return 0
        sums_ar = [0] * (len(positions) + 1)
        start = 0
        for i in positions:
            end = start + 1
            sums_ar[i] = MinMaxDivision.sum_sublist(start, end, int_ar)
            start = end
        return max(sums_ar)

    sum_cash = {}

    @staticmethod
    def max_sum_sublist_old(positions, int_ar):
        if len(int_ar) == 0:
            return 0
        sums_ar = [0] * (len(positions) + 1)
        start = 0
        i = 0
        for end in positions:
            sums_ar[i] = MinMaxDivision.sum_sublist(start, end, int_ar)
            i += 1
            start = end
        return max(sums_ar)

    sum_cash = {}

    @staticmethod
    def sum_sublist(start, end, int_ar):
        cash_num = start * 1000000 + end
        if MinMaxDivision.sum_cash.get(cash_num, 0) == 0:
            result = 0
            for i in range(start, end):
                result += int_ar[i]
            MinMaxDivision.sum_cash[cash_num] = result

        return MinMaxDivision.sum_cash[cash_num]

    @staticmethod
    def test():
        A = [0] * 7
        A[0] = 2
        A[1] = 1
        A[2] = 5
        A[3] = 1
        A[4] = 2
        A[5] = 2
        A[6] = 2
        K = 3
        M = 5
        print(MinMaxDivision.solution(K, M, A))  # 6


# MinMaxDivision.test()

ids = [1, 2, 3]
str_var = '''
            SELECT product_id, product_manual_data
            FROM product
            WHERE product_id IN {}
        '''.format(tuple(ids))

print(str_var)

