"""
    match or search text for a specific pattern
"""

text = 'yeah, but no, but yeah, but no, but yeah'

# Exact Match
print(text =='yeah')
# Search for the location of the first occurrence
print(text.find("no"))

import re

date_pattern = re.compile(r'\d+/\d+/\d+')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(date_pattern.findall(text))