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