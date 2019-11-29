
############ Lesson 5 - 2 ###############################################
"""
 GenomicRangeQuery
https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/



A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

        The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
        The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
        The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.

Write a function:

    def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        M is an integer within the range [1..50,000];
        each element of arrays P, Q is an integer within the range [0..N − 1];
        P[K] ≤ Q[K], where 0 ≤ K < M;
        string S consists only of upper-case English letters A, C, G, T.




"""

class GenomicRangeQuery:

    @staticmethod
    def solution_bad(dna_str, start_points, end_points):
        result = []
        dna_map = {
            "A": 1,
            "C": 2,
            "G": 3,
            "T": 4
        }
        abs_min = 1
        #dna_ar = list(map(lambda x: dna_map[x], dna_str))
        dna_ar = dna_str
        for i in range(0, len(start_points)):
            temp_min = "T"
            #temp_min = 4
            for j in range(start_points[i], end_points[i] + 1):
                if dna_ar[j] < temp_min:
                    temp_min = dna_ar[j]
                if temp_min == abs_min:
                    break
            result.append(dna_map[temp_min])
            #result.append(temp_min)
        return result

    @staticmethod
    def solution(S, P, Q):
        cost_dict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

        curr_counts = [0, 0, 0, 0]
        counts = [curr_counts[:]]
        for s in S:
            curr_counts[cost_dict[s] - 1] += 1
            counts.append(curr_counts[:])

        results = []
        for i in range(len(Q)):
            counts_q = counts[Q[i] + 1]
            counts_p = counts[P[i]]

            if Q[i] == P[i]:
                results.append(cost_dict[S[Q[i]]])
            elif counts_q[0] > counts_p[0]:
                 results.append(1)
            elif counts_q[1] > counts_p[1]:
                results.append(2)
            elif counts_q[2] > counts_p[2]:
                results.append(3)
            elif counts_q[3] > counts_p[3]:
                results.append(4)

        return results

    @staticmethod
    def test():
        S = "CAGCCTA"
        # S = "G" * 100000000
        P = [0] * 3
        Q = [0] * 3
        P[0] = 2
        Q[0] = 4
        P[1] = 5
        Q[1] = 5
        P[2] = 0
        Q[2] = 6

        # P[0] = 0
        # Q[0] = 10000000
        # P[1] = 0
        # Q[1] = 10000000
        # P[2] = 0
        # Q[2] = 10000000
        print(GenomicRangeQuery.solution_bad(S, P, Q))
        print(GenomicRangeQuery.solution(S, P, Q))

GenomicRangeQuery.test()


############ Lesson 5 - 3 ###############################################
"""
MinAvgTwoSlice
https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/


A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

        slice (1, 2), whose average is (2 + 2) / 2 = 2;
        slice (3, 4), whose average is (5 + 1) / 2 = 3;
        slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−10,000..10,000].


"""

class MinAvgTwoSlice:

    # the task was not set clearly
    # solution - 100%
    @staticmethod
    def solution(given_array):
        # min given_array len is 2
        min_average = (given_array[0] + given_array[1]) / 2
        count = 0
        result = 0
        for i in range(1, len(given_array) - 1):
            temp_sum = (given_array[i] + given_array[i + 1]) / 2
            if temp_sum < min_average:
                min_average = temp_sum
            result = i

        for i in range(1, len(given_array) - 2):
            temp_sum = (given_array[i] + given_array[i + 1] + given_array[i + 2]) / 3
            if temp_sum < min_average:
                min_average = temp_sum
            result = i

        return result

    @staticmethod
    def test():
        A = [0] * 7
        A[0] = 4
        A[1] = 2
        A[2] = 2
        A[3] = 5
        A[4] = 1
        A[5] = 5
        A[6] = 8
        print(MinAvgTwoSlice.solution(A))

MinAvgTwoSlice.test()

############ Lesson 5 - 4 ###############################################
"""
CountDiv
https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/


Write a function:

    class Solution { public int solution(int A, int B, int K); }

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.

"""

class CountDiv:
    @staticmethod
    def solution_bad(start_ind, end_ind, div_value):
        result = 0
        first_div = True
        while start_ind <= end_ind:
            if first_div:
                rest_div = start_ind % div_value
                first_div = False
                start_ind += rest_div
            else:
                result += 1
                start_ind += div_value
        return result

    # solution - 100%
    # best solution by mysefl = 100%
    @staticmethod
    def solution(start_ind, end_ind, div_value):
        result = 0
        delta = start_ind % div_value

        if delta == 0:
            result += 1
        diff = end_ind - start_ind + delta
        result += (diff // div_value)
        return result

    @staticmethod
    def test():
        # A = 6
        # B = 12
        # K = 2
        A = 11
        B = 345
        K = 17
        print(CountDiv.solution_bad(A, B, K))  # 20
        print(CountDiv.solution(A, B, K)) # 20

CountDiv.test()
