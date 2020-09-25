"""
    trying to match a text pattern using regular expressions, but it is identifying the longest possible matches of a pattern.
    would like to change it to find the shrtest possible match
"""
import re
str_pattern = re.compile(r'\"(.*)\"')
text = 'Computer says "no."'
print(str_pattern.findall(text))
text2 = 'Computer says "no.", Phone says "yes."'
print(str_pattern.findall(text2))

str_pattern = re.compile(r'\"(.*?)\"')
print(str_pattern.findall(text2))
