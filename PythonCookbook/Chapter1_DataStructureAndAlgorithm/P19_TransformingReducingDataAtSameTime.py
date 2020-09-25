"""
    need to execute a reduction function, but first need to transform or filter data
    Use generator-expression
"""

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

