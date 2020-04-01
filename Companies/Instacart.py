"""
Challenge #3

Write an in-memory, key-value store that can "time travel." This can build off of Challenge #2.



Support 'fuzzy' matching on a timestamp.

kv = KV.new
timestamp = kv.set('foo', 'bar')
sleep(1)
kv.set('foo', 'bar2')

# The case of no timestamp should continue to return the latest set value
kv.get('foo')
=> "bar2"

# Fetch the key 'foo' with the initial timestamp, plus 750 milliseconds
kv.get('foo', timestamp + 0.75)

=> "bar" # returns the closest set value to that timestamp, but always in the past



**** Note: a number of languages have a 2 or 3 second timeout ***

These include C, C++, C++14, C#, Objective-C, Swift, OCaml, and COBOL.

Full list: https://www.hackerrank.com/environment

"""

from collections import defaultdict
from collections import OrderedDict
from datetime import datetime
import time
# https://stackoverflow.com/questions/38558288/set-get-and-popitem-performance-of-ordereddict

class CashData:
    LATEST_KEY = "LATES"

    def __init__(self):
        # self.data_dict = defaultdict({})
        self.data_dict = defaultdict(str, '')

    def set(self, key, value):
        time_dict = self.data_dict[key]
        if not time_dict:
            time_dict = OrderedDict()
        time_dict[CashData.LATEST_KEY] = value
        now = repr(datetime.now())
        time_dict[now] = value
        self.data_dict[key] = time_dict
        return now

    def get(self, key, timestamp=None):
        time_dict = self.data_dict[key]
        if not time_dict:
            return ''

        if not timestamp:
            return time_dict[CashData.LATEST_KEY]
        elif time_dict.get(timestamp, False):
            return time_dict[timestamp]
        else:
            for time_key, value in reversed(time_dict.items()):
                if time_key != CashData.LATEST_KEY and time_key < timestamp:
                    return value
            return None  # time_dict[CashData.LATEST_KEY]


# Case 1
test_obj = CashData()
now_00 = repr(datetime.now())
time.sleep(1)
now_0 = test_obj.set('foo', 'bar0')
time.sleep(1)
now_1 = test_obj.set('foo', 'bar2')
time.sleep(1)
now_fuz = repr(datetime.now())
time.sleep(1)
now_2 = test_obj.set('foo', 'bar3')
time.sleep(1)

print(test_obj.get('foo', now_00))
print(test_obj.get('foo', now_fuz))

# print(test_obj.get('foo'))
# print(test_obj.get('foo', now_1))
# print(test_obj.get('foo', now_0))


# print(test_obj.get('nokey'))

