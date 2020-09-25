"""
    have a data inside of a sequence, and need to extract values or reduce the sequence using some criteria
"""

my_list = [1, 4, -5, 7, 10, -7, 2, 3, -1]

print([n for n in my_list if n > 0])
print([n for n in my_list if n < 0])
