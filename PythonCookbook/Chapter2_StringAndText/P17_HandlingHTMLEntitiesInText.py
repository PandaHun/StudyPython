"""
    replace HTML entities such as &entity
"""

s = 'elements are written as "<tag>tag</tag>".'

import html
print(s)
print(html.escape(s))