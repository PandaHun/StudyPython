"""
    split a string into fields, but the delimiters arn't consistent
"""

line = 'asdf fjdk; afed, fjek,asdf,  foo'
import re
print(re.split(r'[;,\s]\s*', line))