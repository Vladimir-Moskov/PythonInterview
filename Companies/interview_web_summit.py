# Implement the Logger which could be used in server side application
# for logging each request running time. It can be assumed that each
# request has access to Logger and its two public methods:
# request_start and request_end, both accepting a unique request id as parameter.

# get_by_id

# 1    3     6     11
# R1   R2               request_start
#            R2    R1   request_end

# R1: 10s     R2: 3s
# R2  3s      R1: 10s

# 6 R2  - R2 R1 - no print
# 11 R1 - R2 R1 - print

# r1 r2 r3  r3 r1 r2
# r1 r2 r3  r3 r2 r1

from collections import namedtuple
from collections import deque
import time

RequestTime = namedtuple('RequestTime', 'id, start_time, end_time, order')


class LoggerSimple:

    def __init__(self):
        self.request_data = {}  # {request_id: {start_time: value, end_time: value, order: int_value}}

    def request_start(self, request_id):
        self.request_order.append(request_id)
        self.request_data[request_id] = RequestTime(request_id, time.time(), None, len(self.request_data))

    def request_end(self, request_id):
        request_item = self.request_data[request_id]
        request_item.end_time = time.time()
        duration = request_item.end_time - request_item.start_time
        print(f'Request {request_id} duration = {duration} mls, order = {request_item.order}')


class LoggerOrder:

    def __init__(self):
        self.request_data = {}  # {request_id: {start_time: value, end_time: value, order: int_value}}
        self.request_deque = deque()  # not finished requests
        self.print_deque = deque()  #  finished requests

    def request_start(self, request_id):
        new_item = RequestTime(time.time(), None, len(self.request_order))
        self.request_data[request_id] =new_item
        self.request_deque.push(new_item)

    def request_end(self, request_id):
        request_item = self.request_data[request_id]
        request_item.end_time = time.time()
        self.print_deque.push(request_item)
        while len(self.print_deque) > 0 and self.print_deque[-1] == self.request_deque[0]:
            self.print_request_by_id(self.request_deque.popleft())
            self.print_deque.popleft()

    def print_request_by_id(self, request_item):
        duration = request_item.end_time - request_item.start_time
        print(f'Request {request_item.id} duration = {duration} mls, order = {request_item.order}')















