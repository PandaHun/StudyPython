text = '## \
# User Database  \
#\
# Note that this file is consulted directly only when the system is running\
# in single-user mode. At other times, this information is provided by\
# Open Directory.\
...\
##\
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

from itertools import dropwhile, islice
with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end=' ')

items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)