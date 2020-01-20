#############################################
# https://www.hackerrank.com/challenges/string-reduction/problem


def stringReduction_bad(given_str):
    chat_dic = {
        'a': {
            'b': 'c',
            'c': 'b'
        },
        'b': {
            'a': 'c',
            'c': 'a'
        },
        'c': {
            'b': 'a',
            'a': 'b'
        },
    }

    str_ar = list(given_str)
    if len(str_ar) < 2:
        return len(str_ar)
    start_index = 0

    while start_index < (len(str_ar) - 1):
        cur_char = str_ar[start_index]
        next_char = str_ar[start_index + 1]
        if cur_char == next_char:
            start_index += 1
        else:
            new_char = chat_dic[cur_char][next_char]
            str_ar[start_index + 1] = new_char
            str_ar.pop(start_index)
            start_index = max(0, start_index - 1)

    result = len(str_ar)
    return result


def stringReduction(given_str):
    from collections import Counter, defaultdict
    char_count = Counter(given_str)
    if len(char_count) == 1:
        return len(given_str)
    else:
        all_odd_even = char_count.get('a', 0) % 2 + char_count.get('b', 0) % 2 + char_count.get('c', 0) % 2
        if all_odd_even == 0 or all_odd_even == 3:
            return 2
        else:
            return 1


case_0 = "abcbcba"  # 0
case_1 = "aab"  # 2
case_2 = "bcab"  # 1
case_3 = "ccccc"  # 5
case_4 = "babcbbaabcbcbcbaabbccaacccbbbcaaacabbbbaaaccbcccacbbccaccbbaacaccbabcaaaacaccacbaacc"  #
case_5 = "acaacababbcbabbbbbaaaabacaabbcbac"
case_6 = "bcbcacacbbaaccbaacbccaca"
# print(stringReduction(case_0))
# print(stringReduction(case_1))
# print(stringReduction(case_2))
# print(stringReduction(case_3))
# print(stringReduction(case_4))
# print(stringReduction(case_5))
# print(stringReduction(case_6))

#########################################################
# Common Child
# https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

def commonChild_bad(str_val_1, str_val_2):
    mach_matrix = [[0 for _ in range(len(str_val_1) + 1)] for _ in range(len(str_val_2) + 1)]
    for j, char_2 in enumerate(str_val_2, 1):
        for i, char_1 in enumerate(str_val_1, 1):
            if char_1 == char_2:
                mach_matrix[j][i] = mach_matrix[j - 1][i - 1] + 1
            else:
                mach_matrix[j][i] = max(mach_matrix[j-1][i], mach_matrix[j][i-1])

    result = mach_matrix[-1][-1]

    return result

def commonChild(s1, s2):
    m, n = len(s1), len(s2)
    prev, cur = [0]*(n+1), [0]*(n+1)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                cur[j] = 1 + prev[j-1]
            else:
                if cur[j-1] > prev[j]:
                    cur[j] = cur[j-1]
                else:
                    cur[j] = prev[j]
        cur, prev = prev, cur
    return prev[n]


case_00 = "TERRACED"  # 5
case_00_2 = "CRATERED"
case_0 = "HARRY"  # 2
case_0_2 = "SALLY"
case_1 = "SHINCHAN"  # 3
case_1_2 = "NOHARAAA"
case_2 = "ABCDEF"
case_2_2 = "FBDAMN"  # 2
case_3 = "AA"
case_3_2 = "BB"  # 0
#
case_4 = "WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS"
case_4_2 = "FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC"  # 15

print(commonChild(case_00, case_00_2))
print(commonChild(case_0, case_0_2))
print(commonChild(case_1, case_1_2))
print(commonChild(case_2, case_2_2))
print(commonChild(case_3, case_3_2))
print(commonChild(case_4, case_4_2))




#######################################
# https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
def triplets(arr_a, arr_b, arr_c):
    def index_max(set_int, val, start_index):
        set_len = len(set_int)
        for i in range(start_index, set_len):
            set_val = set_int[i]
            if set_val > val:
                return i
        return set_len

    result = 0
    set_a = sorted(set(arr_a))
    set_b = sorted(set(arr_b))
    set_c = sorted(set(arr_c))
    a_index = 0
    c_index = 0
    for val_b in set_b:
        a_index = index_max(arr_a, val_b, a_index)
        c_index = index_max(arr_c, val_b, c_index)
        result += a_index * c_index

    return result

# 8
case_1_1 = [1, 3, 5]
case_1_2 = [2, 3]
case_1_3 = [1, 2, 3]

# 5
case_2_1 = [1, 4, 5]
case_2_2 = [2, 3, 3]
case_2_3 = [1, 2, 3]

# 12
case_3_1 = [1, 3, 5, 7]
case_3_2 = [5, 7, 9]
case_3_3 = [7, 9, 11, 13]
# print(triplets(case_1_1, case_1_2, case_1_3))
# print(triplets(case_2_1, case_2_2, case_2_3))
print(triplets(case_3_1, case_3_2, case_3_3))

#######################################

