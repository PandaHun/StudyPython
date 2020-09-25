"""
    need to check the start or end of a string for specific text pattern
"""

filename = 'spam.txt'
print(filename.endswith('txt'))
print(filename.startswith('file:'))

filenames = ['make', 'foo.c', 'foo.h', 'bar.py']
print([name for name in filenames if name.endswith(('.c', '.h'))])

choices = ['http:', 'ftp:']
url = 'http://url'
#print(url.startswith(choices))
"""
    It had occured Exception
    Exception has occurred: TypeError
    startswith first arg must be str or a tuple of str, not list
"""
print(url.startswith(tuple(choices)))