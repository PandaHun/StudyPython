"""
    find out what they have in common(same keys, same values, etc...)
"""

a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print(a.keys() & b.keys())

print(a.keys() - b.keys())

print(a.items() & b.items())

c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)