import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    for path, _, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)

def gen_opener(filenames):
    for filename in filenames:
        if (filename.endswith('.gz')):
            f = gzip.open(filename, 'rt')
        elif (filename.endswith('.bz2')):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()

def gen_concentrate(iterators):
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concentrate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)