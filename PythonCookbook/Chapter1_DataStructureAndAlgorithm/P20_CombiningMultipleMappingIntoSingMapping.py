"""
    multiple dictionaries or mappings that want to logically combine into a single mapping to perform certain operations.
    such as looking up values or checking for the existence of keys
    using ChainMap
"""

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap

c = ChainMap(a,b)
print(c['x'])
print(c['z'])
print(c)