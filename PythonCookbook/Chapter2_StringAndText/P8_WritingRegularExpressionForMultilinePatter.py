"""
    try to match a block of text using a regular expressions, but you need the match to span multiple lines
"""
import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
... multiline comment */
'''

print(comment.findall(text1))
print(comment.findall(text2))
"""
    expect ' this is a ... multiline comment ', then []
    to fix the problem
"""
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))