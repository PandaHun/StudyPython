"""
    eliminate the duplicate values in sequence, but preserve the order of the remaining itmes
"""


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

"""
    eliminate the duplicate is able to use set, but this approach doesn't preserve any kind of ordering
    So data will be scrabled afterward
"""

print(set(a))