list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

data = zip(list1, list2)
print(data)
data = sorted(data)
print(data)

#parallel sorting list
list1, list2 = map(lambda t: list(t), zip(*data))
print(list1)
print(list2)
