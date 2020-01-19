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
print(stringReduction(case_1))
# print(stringReduction(case_2))
# print(stringReduction(case_3))
# print(stringReduction(case_4))
# print(stringReduction(case_5))
# print(stringReduction(case_6))

#########################################################
