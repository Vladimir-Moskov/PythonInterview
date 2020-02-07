# print('abcd'.translate('a'.maketrans('abc', 'bcd')))

z = set('abc')
z.add('san')
z.update(set(['p', 'q']))
print(z)

a = {1: "A", 2: "B", 3: "C"}
b = a.copy()
b[2] = "D"
print(a)

print("Hello {} and {}".format('joe', 'doe'))
print('new' 'line')

lst = [3, 4, 6, 1, 2]
lst[1:2] = [7, 8]
print(lst)

alphabets = 'abcd'
for i in range(len(alphabets)):
    print(alphabets)
    alphabets = 'a'

print('yz90'.isalnum())

print("Hello {0!r} and {1!s}".format('john', 'doe'))

print('helo'.partition('lo'))

print("%-006d" % 456)

print(~101)

a = (2, 3, 4)
print(sum(a, 3))

print('abc'.encode())


def writer():
    title = 'Sir'
    name = (lambda x: title + ' ' + x)
    return name


who = writer()
print(who('Arthur'))

x = 3
print(eval('x^2'))

print("-%006d" % -122)

for i in [1, 2, 3, 4][::-1]:
    print(i)

print('{:,}'.format(1112223334))

str1 = 'hello'
print(str1[-1:])

print('xyyzxxyxyy'.lstrip('xyy'))

a = [1, 4, 3, 5, 2]
b = [3, 1, 5, 2, 4]
a == b
print(set(a) == set(b))
