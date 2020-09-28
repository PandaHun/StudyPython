from itertools import permutations, combinations

items = ['a', 'b', 'c']
for p in permutations(items, 2):
    print(p)

for c in combinations(items, 2):
    print(c)