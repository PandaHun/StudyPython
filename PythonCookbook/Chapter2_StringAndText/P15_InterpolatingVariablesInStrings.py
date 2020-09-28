"""
    create a string in which embedded variable names are substituted with a string represnetation of a variable's value
"""

s = '{name} has {n} messages'
print(s.format(name="Guido", n=37))
name = 'bao'
n = 26
print(s.format_map(vars()))
print(s.format(vars()))