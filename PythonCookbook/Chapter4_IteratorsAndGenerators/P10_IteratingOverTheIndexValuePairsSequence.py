my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

for idx, val in enumerate(my_list, 2):
    print(idx, val)


idx = 0
for val in my_list:
    ...
    idx += 1
