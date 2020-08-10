######################################################################
# https://www.hackerrank.com/challenges/the-power-sum/problem
# The Power Sum
#

import math


def powerSum(X, N):
    result = 0
    x_root_n = int(X ** (1 / N))
    arr_pow_n = [0] * (x_root_n + 1)

    for i in range(x_root_n + 1):
        arr_pow_n[i] = i ** N

    result = check_val(arr_pow_n, 1, X)

    return result

def check_val(arr, cur_index, cur_val):
    result = 0
    if cur_index < len(arr):
        for i in range(cur_index, len(arr)):
            if arr[i] == cur_val:
                result += 1
                break
            elif arr[cur_index] > cur_val:
                break
            else:
                result += check_val(arr, i + 1, cur_val - arr[i])
    return result



# print(powerSum(10, 2))  # 1
# print(powerSum(100, 2))  # 3
# print(powerSum(100, 3))  # 1

######################################################################
# https://www.hackerrank.com/challenges/crossword-puzzle/problem
# Crossword Puzzle


def crosswordPuzzle(crossword, words):
    result = []
    words_ar = words.split(";")
    crossword_ar = [list(line) for line in crossword]

    result = recurcive_search(words_ar, crossword_ar)

    return ["".join(line) for line in crossword_ar]


def recurcive_search(words_ar, crossword_ar, current_word_index=0):
    if current_word_index == len(words_ar):
        return True

    word = words_ar[current_word_index]
    for i in range(len(crossword_ar)):
        for j in range(len(crossword_ar[0])):
            if crossword_ar[i][j] == "-" or crossword_ar[i][j] == word[0]:
                start_with = crossword_ar[i][j] == word[0]
                if (j == 0 or crossword_ar[i][j-1] != "-") and (j + 1 < len(crossword_ar[0]) and (crossword_ar[i][j+1] == "-" or (not start_with and word[1] == crossword_ar[i][j+1]))):
                    k = 1
                    while (j + k) < min(j + len(word), len(crossword_ar[0])) and (crossword_ar[i][j + k] == "-" or crossword_ar[i][j + k] == word[k]) :
                        k += 1
                    if k == len(word):
                        k = 1
                        for k in range(len(word)):
                            crossword_ar[i][j + k] = word[k]
                        is_fit = recurcive_search(words_ar, crossword_ar, current_word_index + 1)
                        if not is_fit:
                            for k in range(len(word)):
                                crossword_ar[i][j + k] = "-"
                            if start_with:
                                crossword_ar[i][j] = word[0]
                        else:
                            return True

                elif (i == 0 or crossword_ar[i-1][j] != "-") and (i + 1 < len(crossword_ar) and (crossword_ar[i+1][j] == "-" or (not start_with and word[1] == crossword_ar[i+1][j]))):
                    k = 1
                    while (i + k) < min(i + len(word), len(crossword_ar)) and (crossword_ar[i + k][j] == "-" or crossword_ar[i+k][j] == word[k]):
                        k += 1
                    if k == len(word):
                        k = 1
                        for k in range(len(word)):
                            crossword_ar[i + k][j] = word[k]

                        is_fit = recurcive_search(words_ar, crossword_ar, current_word_index + 1)
                        if not is_fit:
                            for k in range(len(word)):
                                crossword_ar[i+k][j] = "-"
                            if start_with:
                                crossword_ar[i][j] = word[0]
                        else:
                            return True

    return False


# case 1
crossword = [
    "+-++++++++",
    "+-++++++++",
    "+-++++++++",
    "+-----++++",
    "+-+++-++++",
    "+-+++-++++",
    "+++++-++++",
    "++------++",
    "+++++-++++",
    "+++++-++++"
]
words = "LONDON;DELHI;ICELAND;ANKARA"

# case 2
crossword = [
    "+-++++++++",
    "+-++++++++",
    "+-------++",
    "+-++++++++",
    "+-++++++++",
    "+------+++",
    "+-+++-++++",
    "+++++-++++",
    "+++++-++++",
    "++++++++++"
]
words = "AGRA;NORWAY;ENGLAND;GWALIOR"


crossword = [
    "+-++++++++",
    "+-++-+++++",
    "+-------++",
    "+-++-+++++",
    "+-++-+++++",
    "+-++-+++++",
    "++++-+++++",
    "++++-+++++",
    "++++++++++",
    "----------"
]
words = "CALIFORNIA;NIGERIA;CANADA;TELAVIV"
print(crosswordPuzzle(crossword, words))

######################################################################


















