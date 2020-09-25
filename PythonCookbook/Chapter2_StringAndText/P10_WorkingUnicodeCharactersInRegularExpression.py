"""
    using regular expressions to process text, but are concerned about the handling of Unicode characters
"""
import re
num = re.compile(r'\d+')
print(num.match('123'))
print(num.match('\u0661\u0662\u0663'))