# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S, K):
    days_list = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    days_dic = {
        "Mon": 0,
        "Tue": 1,
        "Wed": 2,
        "Thu": 3,
        "Fri": 4,
        "Sat": 5,
        "Sun": 6}

    day = (K - (7 - days_dic[S])) % 7
    return days_list[day]


"""
-- write your code in PostgreSQL 9.4
SELECT MAX((SELECT COUNT(*) FROM meetings WHERE 
    (start_time >= main.start_time and start_time <= main.end_time)
   
    )) as room_amount
    
FROM meetings as main

"""

"""
\b[0-9]{3}-[0-9]{3}-[0-9]{3}\b
"""