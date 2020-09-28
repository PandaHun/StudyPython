from datetime import datetime
from pytz import timezone

d = datetime(2020, 9, 21, 9, 30, 0)
print(d)

central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)
seo_d = loc_d.astimezone(timezone('Asia/Seoul'))
print(seo_d)
