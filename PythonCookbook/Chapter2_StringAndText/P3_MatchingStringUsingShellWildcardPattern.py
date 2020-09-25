"""
    match text using the same wildcard patterns as are commonly used when working in shell
"""

from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.TXT'))
print(fnmatchcase('foo.txt', '*.TXT'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

print([name for name in names if fnmatch(name, 'Dat*.csv')])