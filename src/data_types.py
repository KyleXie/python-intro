# Numbers

2 + 2

50 - 5*6

5 // 2

2 ** 10


# Strings

'Hello World'

name = 'Beijing'

greeting = f'Hello, {name}'

greeting.split(',')

greeting[2]

greeting[2:5]

greeting[2:]

greeting[-1]

greeting[:-3]

greeting[::-1]

"""
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""

'ello' in greeting

'hello' + 'world'

'hello' * 2


# Lists

[1, 2, 3, 'a', 'b', 4, 5]

[1, 2, 'a'] + [3, 'b', 5]

a_list = [1, 2, 3, 'a', 'b', 4, 5]
len(a_list)
a_list[0]
a_list[2:5]
del a_list[2:5]

a_list.sort()
a_list = sorted(a_list)

# List Comprehensions
[x * 2 for x in a_list if isinstance(x, int)]

for item in a_list:
    print(item)


for item in reversed(a_list):
    print(item)


for index, item in enumerate(a_list):
    print(index, item)


another_list = ['一', '二', '三', '四']

for item1, item2 in zip(a_list, another_list):
    print(item1, item2)

a_tuple = (1, 2, 3, 'a', 'b', 4, 5)

a, b = 1, 2
a == b
a is b


# Dicts
tel = {'jack': 4098, 'sape': 4139}
tel = dict(jack=4098, sape=4139)
tel['gudio'] = 5000
tel['gudio']
tel.get('gudio')

{x: x * 2 for x in [1, 2, 3]}

for key, value in tel.items():
    print(key, value)


