import heapq
from heapq import merge
a = [1, 4, 17, 18]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)

a = [2, 4, 1, 5]
b = [3, 5, 4 ,1]
for c in heapq.merge(a, b):
    print(c)