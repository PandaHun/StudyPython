'''
    If have an N-elements Tuple or Sequence
    unpack into a collection of N variables
'''

data = ['ACNE', 50, 91.1, (2020, 9, 21)]
name, shares, price, date = data
print(name)
print(date)

name, shares, price, (year, month, day) = data
print(year)
print(month)

'''
    Unpacking works with Object, tuple, files, Strings any to be iterable
    And then, should discard certain values
'''

_, shares, price, _ = data
print(shares)
print(price)