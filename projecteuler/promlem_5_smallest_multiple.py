# https://projecteuler.net/problem=5
# https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem

from functools import reduce

def solition(range_val):
    result = 0
    res_ar = []
    all_num = list(range(2, range_val + 1))
    while len(all_num) > 0:
        cur_num = all_num[len(all_num) - 1]
        all_num.remove(cur_num)
        res_ar.append(cur_num)
        for j in all_num:
            if cur_num % j == 0:
                all_num.remove(j)
    result = reduce((lambda x, y: x * y), res_ar)

    can_div = False
    sub = [result]
    index = 0
    res_ar = list(range(2, range_val + 1))
    while index < len(sub):
        result = sub[index]
        has_div = False
        for y in res_ar:
            max_val = result // y
            can_div = True
            for x in res_ar:
                if max_val % x != 0:
                    can_div = False
                    break
            if can_div:
                has_div = True
                sub.append(max_val)

        if not has_div:
            index += 1
        else:
            sub.pop(index)
    result = min(sub)


    return result

#print(solition(20))
#  232792560
# 1862340480
# 670442572800
#  33522128640.0, 37246809600.0, 41902660800.0, 44696171520.0, 55870214400.0]

print(solition(10))