from datetime import datetime, timedelta
a = timedelta(days=2, hours=6)
print(a)
print(a.seconds)
b = datetime(2020, 9, 23)
c = datetime(2020, 12, 21)
d = c - b
print(d.days)
print(b)
print(b.day)
