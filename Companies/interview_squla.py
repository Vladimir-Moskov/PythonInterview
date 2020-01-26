# Company Squla - Amsterdam, Netherlands
# Date: 2020-01-21
# https://app.codility.com/c/feedback/XWZ28J-283/


# def solution(phone_numbers, phone_owners, number):
#     """
#         solution time complexity - O(n)
#         I dont get it, is it just too simple or I have missed something important,
#          - 'phone number format nnn-nnn-nnn' has not been used :(
#         I will check it later
#
#         if phone_numbers has dublicates with different owners it will returns only first one
#     """
#     for i, phone in enumerate(phone_numbers):
#         if phone == number:
#             return phone_owners[i]
#
#     return number


def solution(lower_case_chars):
    """
        this is a good one - total time complexity O(n), which is the minimum,
        but code can be optimize a little bit
    """
    from collections import Counter
    result = 0
    # O(n)
    char_counter = Counter(lower_case_chars)
    set_helper = set()
    # O(1), because 24 items in char_counter is the worst case
    for key, val in char_counter.items():
        while val > 0 and val in set_helper:
            val -= 1
            result += 1
        if val > 0:
            set_helper.add(val)
    return result


case_1 = "aaaabbbb"
print(solution(case_1))
case_2 = "ccaaffddecee"
print(solution(case_2))
case_3 = "eeee"
print(solution(case_3))
case_4 = "example"
print(solution(case_4))

# Task 1 	Python 	2020-01-21 22:28:50
# Task 2 	Python 	2020-01-21 22:22:09
# Task 3 	SQL (PostgreSQL) 	2020-01-21 22:17:49
# Test link
#
# You can use your test link to see this summary later.
# Your link will be active until  2020-02-21.


# Take longer - I have not played with postgresql for a while

#
# SELECT
#     task_id,
#     task_name,
#     (CASE
#          WHEN average_score <= 20 THEN 'Hard'
#          WHEN average_score > 60 THEN 'Easy'
#          ELSE 'Medium'
#      END) as difficulty
#
#     FROM(
#         SELECT
#                 tasks.id as task_id,
#                 tasks.name as task_name,
#                 (SELECT coalesce(avg(reports.score), 0)
#                 FROM reports
#                 WHERE tasks.id = reports.task_id) as average_score
#     FROM tasks
#     WHERE EXISTS(SELECT * FROM reports
#                 WHERE reports.task_id = tasks.id )) as tasks_avga
















