'''
    make a dictionary that maps keys to more than one value
    => multidict
    as a list or set
'''

from collections import defaultdict
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}
print(d)

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
