# https://www.hackerrank.com/challenges/richie-rich/problem
# Highest Value Palindrome


def solution_Highest_Value_Palindrome():
    def highestValuePalindrome(str_val, str_len, shifts_num):
        mid_val = int(str_len / 2)
        result = [0] * mid_val
        changes_dic = {}
        for i in range(mid_val):
            if str_val[i] != str_val[-(i + 1)]:
                result[i] = max(str_val[i], str_val[-(i + 1)])
                shifts_num -= 1
                changes_dic[i] = 1
            else:
                result[i] = str_val[i]
                changes_dic[i] = 0
        if shifts_num < 0:
            return "-1"

        elif shifts_num > 0:
            for i in range(mid_val):
                if shifts_num > 0:
                    if result[i] != '9':
                        if shifts_num + changes_dic[i] > 1:
                            result[i] = '9'
                            shifts_num -= (2 - changes_dic[i])
                else:
                    break
        result.extend(reversed(result))
        if str_len % 2 == 1:
            if shifts_num > 0:
                result.insert(mid_val,"9")
            else:
                result.insert(mid_val, str_val[mid_val])

        return "".join(result)

    shifts_num = 1
    str_len = 4
    str_val = "3943"  # 3993
    print(highestValuePalindrome(str_val, str_len, shifts_num))
    shifts_num = 3
    str_len = 6
    str_val = "092282"  # 992299
    print(highestValuePalindrome(str_val, str_len, shifts_num))
    shifts_num = 1
    str_len = 4
    str_val = "0011"  # -1
    print(highestValuePalindrome(str_val, str_len, shifts_num))
    shifts_num = 1
    str_len = 1
    str_val = "5"  # 9
    print(highestValuePalindrome(str_val, str_len, shifts_num))

    shifts_num = 2
    str_len = 6
    str_val = "932239"  # 9
    print(highestValuePalindrome(str_val, str_len, shifts_num))

    shifts_num = 1
    str_len = 5
    str_val = "12321"  # 9
    print(highestValuePalindrome(str_val, str_len, shifts_num))


    shifts_num = 0
    str_len = 3
    str_val = "777"  # 9
    print(highestValuePalindrome(str_val, str_len, shifts_num))

####################################################################################################
# https://www.hackerrank.com/challenges/maximum-palindromes/problem
# Maximum Palindromes

def solutionMaximumPalindromes1():
    def initialize(s):
        global arr, fac, mod, M
        M = 1000000007
        n = len(s)
        arr = [[0 for _ in range(n + 1)] for _ in range(26)]
        for i in range(n):
            for j in range(26):
                arr[j][i + 1] = arr[j][i] + ((ord(s[i]) - 97) == j)
        fac = [1] * (n + 1)
        mod = [1] * (n + 1)
        for i in range(1, n + 1):
            fac[i] = (fac[i - 1] * i) % M
            mod[i] = pow(fac[i], M - 2, M)

    def answerQuery(l, r):
        global arr, fac, mod, M
        odd = 0
        even = 0
        divs = 1
        for i in range(26):
            value = arr[i][r] - arr[i][l - 1]
            odd += (value & 1)
            even += (value // 2)
            divs = (divs * mod[value // 2]) % M
        result = (fac[even] * divs) % M
        if (odd > 0):
            result = (result * odd) % M
        return result


def solutionMaximumPalindromes():
    from collections import defaultdict
    result_matrix = None


    def initialize(given_str):
        global result_matrix
        result_matrix = [[0] * len(given_str) for _ in range(len(given_str))]
        factorial = [1] * len(given_str)
        for i in range(1, len(given_str)):
            factorial[i] = i * factorial[i-1]
        for i in range(len(given_str)):
            counter = defaultdict(int)
            counter[given_str[i]] = 1
            pairs_num = 0
            not_pairs_num = 1
            result_matrix[i][i] = 1
            for j in range(i, len(given_str)):
                counter[given_str[j]] += 1
                if counter[given_str[j]] % 2 == 0:
                    pairs_num += 1
                    not_pairs_num -= 1
                else:
                    not_pairs_num += 1

                result_matrix[i][j] = not_pairs_num * factorial[pairs_num]

    def answerQuery(start_ind, end_ind):
        global result_matrix
        result = result_matrix[start_ind - 1][end_ind - 1]
        return result


    initialize('week')

    print(answerQuery(1, 4))  # 2
    print(answerQuery(2, 3))  # 1

####################################################################################################
# https://www.hackerrank.com/challenges/bear-and-steady-gene/problem
# Bear and Steady Gene


# O(n**2) solution -> refactored to O(n) solution
def solutionBearSteadyGene():

    def _steadyGene(gene):
        result = len(gene)
        map_ind = {"A": 0, "C": 1, "G": 2, "T": 3}
        max_count = len(gene) / 4
        calc_matrix = [[0]*4 for _ in range(len(gene))]
        calc_matrix[0][map_ind[gene[0]]] = 1
        overflow_ar = [0] * len(gene)
        overflow_ar2 = [1] * len(gene)
        for i in range(1, len(gene)):
            calc_matrix[i][0] = calc_matrix[i - 1][0]
            calc_matrix[i][1] = calc_matrix[i - 1][1]
            calc_matrix[i][2] = calc_matrix[i - 1][2]
            calc_matrix[i][3] = calc_matrix[i - 1][3]
            calc_matrix[i][map_ind[gene[i]]] += 1
            overflow_ar[i] = overflow_ar[i - 1]
            if calc_matrix[i][map_ind[gene[i]]] > max_count:
                overflow_ar[i] += 1
            overflow_ar2[i] = max(calc_matrix[i]) - min(calc_matrix[i])

        count_replace = overflow_ar[-1]
        over_dic = {}
        for i, ch_count in enumerate(calc_matrix[-1]):
            if ch_count > max_count:
                over_dic[i] = ch_count - max_count
        # O(n^2) search
        # for i in range(len(gene) - count_replace):
        #     for j in range(i, len(gene)):
        #         start = calc_matrix[i]
        #         end = calc_matrix[j]
        #         flag = True
        #         for n, k in over_dic.items():
        #             if end[n] - start[n] < over_dic[n]:
        #                 flag = False
        #                 break
        #         if flag:
        #             result = min(result, (j - i))
        #         if result == count_replace:
        #             return result

        # O(n) search - "moving window" approach
        start = 0
        end = count_replace
        while end < len(gene) and (start < len(gene) - count_replace):
            start_val = calc_matrix[start]
            end_val = calc_matrix[end]
            flag = True
            for n, k in over_dic.items():
                if end_val[n] - start_val[n] < over_dic[n]:
                    flag = False
                    break
            if flag:
                result = min(result, (end - start))
                start += 1
            else:
                end += 1
            if result == count_replace:
                return result

        return result

    from collections import Counter

    def balanced(n, dic):
        bal = True
        for k, v in dic.items():
            if v > n:
                    bal = False
                    break
        return bal

    # O(n) solution
    def steadyGene(gene):
        N = len(gene)
        g_n = N/4
        gene_freq = Counter(gene)

        min_ans = 10**9
        right = left = 0
        while right < N and left < N:
            if not balanced(g_n, gene_freq):
                gene_freq[gene[right]] -= 1
                right += 1
            else:
                min_ans = min(min_ans,  right - left)
                gene_freq[gene[left]] += 1
                left += 1

        return min_ans

    gene = "GAAATAAA" # 5
    print(steadyGene(gene))
    gene = "TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC" # 5
    print(steadyGene(gene))

# solutionBearSteadyGene()

####################################################################################################
# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
# HackerRank in a String!

def hackerrankInString(s):
    main_str = "hackerrank"
    start = 0
    if len(s) >= len(main_str):
        i = 0
        while start < len(main_str) and i < len(s):
            if main_str[start] == s[i]:
                start += 1
            i += 1

    return "YES" if start == len(main_str) else "NO"

####################################################################################################