"""
    Code interview solution for company Booking.com, Amsterdam, Netherlands
    Date: 2019-12-15

    Summary:
        score is  about 80% with www.hackerrank.com
        No answer so far :(, will retry latter - ;).

    No answer
"""
# Complete the 'multiple' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER y
#  3. INTEGER z
#  4. INTEGER n
#

# def multiple(x, y, z, n):
#     # Write your code here
#     result = []
#
#     for i in range(1, n +1):
#         if z == 0 or i % z != 0:
#             if (x != 0 and i % x == 0) \
#             or (y != 0 and i % y == 0):
#                 result.append(i)
#     return result
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     x = int(input().strip())
#
#     y = int(input().strip())
#
#     z = int(input().strip())
#
#     n = int(input().strip())
#
#     result = multiple(x, y, z, n)
#
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()

import itertools
# matrix1=[[1234, 532632], [234, 632633], [2354, 732634]]
# matrix2=[[1234, 532632], [234, 632633], [458,  642633], [2354, 732634]]
#
# def missingReservations(firstReservationList, secondReservationList):
#     # Write your code here
#     # not optimized solution
#     # irstReservationSet = set(itertools.chain.from_iterable(firstReservationList))
#     # secondReservationSet = set(itertools.chain.from_iterable(secondReservationList))
#     # totalSet = list(itertools.chain(firstReservationSet, secondReservationSet))
#     #result = [x for x in totalSet if x not in firstReservationSet or x not in secondReservationSet]
#     firstNums = [x[0] for x in firstReservationList]
#     secondNums = [x[0] for x in secondReservationList]
#     result = [x for x in secondNums if x not in firstNums]
#     return result
#
# print(missingReservations(matrix1, matrix2))

def employeeWithLesserThanKBreaks(employeeCalls, k):
    # Write your code here
    # hope employeeCalls is ordered
    # needs optimisation - only 20 min left :(
    breaks_dic = {}
    employeeCalls = sorted(employeeCalls, key=lambda item: item[0])
    print(employeeCalls)
    prev_id = 0
    for i, log in enumerate(employeeCalls):
        employee_id = log[0]
        if prev_id != employee_id:
            prev_id = employee_id
            breaks_dic[employee_id] = 0
        else:
            prev_end_time = employeeCalls[i - 1][2]
            start_time = log[1]
            if start_time != prev_end_time:
                breaks_dic[employee_id] += 1

    result = []
    for employee_id in breaks_dic.keys():
        breaks_count = breaks_dic[employee_id]
        if breaks_count < k:
            result.append([employee_id, breaks_count])
    if len(breaks_dic.keys()) == len(result):
        result = []
    return result



#{k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

matr = [
    [1, 1481122000, 1481122020],
[3, 1481122000, 1481122020],
[1, 1481122020, 1481122040],
[2, 1481122020, 1481122040],
[3, 1481122040, 1481122060],
[1, 1481122050, 1481122060],
[3, 1481122070, 1481122090],
    ]
print(employeeWithLesserThanKBreaks(matr, 3))