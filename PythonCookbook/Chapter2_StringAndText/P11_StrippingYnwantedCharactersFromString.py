"""
    strip unwanteds characters, such as whitespace
"""
s = '   hello world   \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())
t = '----hello===='
print(t.strip('-'))
print(t.strip('='))