"""
    less dependent on position in the structure, by accessing elements by name.
    Collections.namedtuple()
"""

from collections import namedtuple

Subscriber = namedtuple('Subcriber', ['addr', 'joined'])
sub = Subscriber('jone@example.com', '2012-10-19')
print(sub)
print(sub.addr)

"""
    namedtuple properties is immutable, if want to change some value then use _replace
"""

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.4)
print(s)
#s.shares = 75
"""
    it throws error
    Exception has occurred: AttributeError  can't set attribute
"""
s = s._replace(shares=76)
print(s)
