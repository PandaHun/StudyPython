"""
    become an unreadalbe mess of hardcoded slice indices and want to clean in up
"""

record = '0123456789012345678901234567890123456789012345678901234567890'
cost = int(record[20:32]) * float(record[40:48])

SHARES = slice(20,32)
PRICE = slice(40,48)
cost = int(record[SHARES]) * float(record[PRICE])