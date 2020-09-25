text = 'yeah, but no, but yeah, but no, but yeah'

print(text.replace('yeah', 'yap'))

"""
    if simple replacing is able to use replace(), but for more complicated pattern, use the sub() in module re
    this example 11/27/2012 to 2012-11-27
"""

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

import re
# Expect Today is 2012-11-27. PyCon starts 2013-3-13.
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

# if more better performance
date_patter = re.compile(r'(\d+)/(\d+)/(\d+)')
print(date_patter.sub(r'\3-\1-\2', text))

# For more complcated subsitutions using callback function

from calendar import month_abbr
def change_date(m):
    mon_nmae= month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_nmae, m.group(3))

