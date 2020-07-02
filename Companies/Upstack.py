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

