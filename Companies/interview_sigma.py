# 1
test_set = {"one", "two", "three"}

test_value = test_set[:2]

# what data do we have in test_value variable ?

{"one", "two"}


# 2
def test_func(param=[]):
    param.append(1)
    print(param)


test_func()  # [1]
test_func()  # [1, 1]
test_func()  # [1, 1, 1]

# what will we get after each test_func call ?
[1, 1, 1]

# 3

a = 2
b = 3

# swap values in variables a and b, i.e a should contains value from b and vice versa

a, b = b, a

# 4

test_string = "   some text     here     and   some      text    here    test ?        "

# expected result is "some text here and some text here test ?"

temp = test_string.split()
result = ' '.join(temp)


class A1(object):
    pass


class A2():
    pass


temp = (1, 2, 3, "4")

my_dict = {temp: "3"}


