#

# Define a List with a few negative and positive numbers.
# Using list comprehensions, obtain the square  values for only the positive numbers from the original list

my_list = [1, -2, 3, -4, 6]
new_list = (x ** 2 for x in my_list if x > 0)

# print(new_list)

# (0, 1), (2, 3) … (N-1, N)
#
# E.g.
# N=5
# (0, 1), (2, 3), (4, 5)
# N=4
# (0, 1), (2, 3)

# next - >


def my_generato(N):
    i, j = 0, 1
    while j <= N:
        yield (i, j)
        i += 2
        j += 2


# for val in my_generato(5):
#     print(val)


# Interviewer
#  - work_start : datetime
#  - work_end : datetime
#  - booked_events: Event[]
#
#
# Event:
#  - start: datetime
#  - duration: int # seconds

from datetime import timedelta, datetime


class Interviewer:

    def __init__(self, work_start, work_end):
        self.work_start = work_start
        self.work_end = work_end
        self.booked_events = []

    def add_event(self, event):
        result = False
        if event.start >= self.work_start and event.end <= self.work_end:
            # O(n) -> O(log n)
            has_overlap = False
            for booked_event in self.booked_events:
                if booked_event.start <= event.start <= booked_event.end or \
                   booked_event.start <= event.end <= booked_event.end or \
                        (booked_event.start > event.start and booked_event.end < event.end):
                    has_overlap = True
                    break
            else:
                self.booked_events.append(event)
                return True

        return False


class Event:

    def __init__(self, start, duration: timedelta):
        self.start = start
        self.duration = duration
        self.end = start + duration


##############################################
# Round 2






def n_uniq_max(given_list, n):
    if n > len(given_list):
        return 0

    val_list = list(set(given_list))
    val_list.sort()

    result = sum(val_list[-n:])

    return result


def n_uniq_max_2(given_list, n):
    if n > len(given_list):
        return 0

    val_dic = {key: 0 for key in given_list}

    if n > len(val_dic.keys()):
        n = len(val_dic.keys())

    max_list = list(val_dic.keys())[:n]
    current_min = max_list[0]
    for val in max_list:
        if current_min > val:
            current_min = val

    for key in list(val_dic.keys())[n:]:
        if key > current_min:
            for i in range(len(max_list)):
                if max_list[i] == current_min:
                    max_list[i] = key

            current_min = max_list[0]
            for val in max_list:
                if current_min > val:
                    current_min = val

    result = 0
    for val in max_list:
        result += val

    return result


import time

def timeit(temed):

    def decorted(*args, **kargs):
        start_time = time.perf_counter()
        result = temed(*args, **kargs)
        print(f"Execution_time = {time.perf_counter() - start_time} ms")
        return result

    decorted.__name__ = temed.__name__
    return decorted


@timeit
def fibonachi(n):
    if n < 2:
        return n

    result = 1
    prev = 0
    current = 1
    for i in range(2, n + 1):
        prev, current = current, prev + current
        result += current

    return result

# print(fibonachi(100))


# print(n_uniq_max_2( [1,2,3,7,23,99,1,2,4,1,15,6,4,99], 3))


from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # a class method to create a Person object by birth year.

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

        # a static method to check if a Person is adult or not.

    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

