'''
    create a dictionary, to control the order of itmes when iteration or serializing
    OrderedDict
'''
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 4
d['bar'] = 3
d['ng'] = 1
d['gro'] = 2

for key in d:
    print(key, d[key])

print(d)