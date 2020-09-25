'''
    Unpack N-elements from an iterable, but the iterable may be longer than N
    then causing "too many values to unpack"
'''
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)

record = ('Bao', 'bao@42maru.com', '010-1234-1234', '+8210-1234-1234')

name, email, *contacts = record
print(contacts)

'''
 * star expressions be useful when combined with certain kinds of String processing
'''

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fileds, homedir, sh = line.split(':')
print(homedir)
print(sh)