"""


    1)     Calculate number of out between 2 dates. Let’s say 11/12/1958 & 10/12/1999

    2)     List out the numbers in particular string. Egg. “50 guy & 17 girl consume average of 122 tons of food every month”

    3)     Create 6*6 matrix with Random int values
            https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/

    4)     Calculate each rows of the matrix you created

    5)     Build datamodel (cow) has below attributes

        Age(Numeric)
        Name(String)
        Alive(Boolean)


    6)     Generate array of 100 of Cows who has random age from 2 to 70

    7)     Create pandas dataframe with 10 columns

    8)     Build Unit test for Calculator method and there might be one error so you need to solve it

"""

from dataclasses import dataclass

@dataclass
class Item:
    field1: int
    field2: str


# 1
from datetime import datetime

date_template = '%d/%m/%Y'
date_str_1 = '11/12/1958'
date_str_2 = '10/12/1999'
datetime_object_1 = datetime.strptime(date_str_1, date_template)
datetime_object_2 = datetime.strptime(date_str_2, date_template)
date_dif = datetime_object_1 - datetime_object_2

print(abs(date_dif.days))

# 3
# generate random integer values
import random
# seed random number generator
# random.seed(1)

values = [[random.randint(0, 10) for _ in range(6)] for _ in range(6)]
print(values)
print(sum([sum(x) for x in values]))

import numpy
# seed random number generator
# numpy.random .seed(1)
# generate some integers
values = numpy.random.randint(0, 10, (6, 6))
print(values)
print(numpy.sum(values))

import pandas

table_col = {'col1': [1], 'col2': [2], 'col3': [3]}

data_frame = pandas.DataFrame(data=table_col)
print(data_frame)

import pytest



# def test_case_1():
#     x = 1
#     assert x == 1, 'test_case_1'
#
# def test_case_2():
#     x = 12
#     assert x == 12, 'test_case_2'
