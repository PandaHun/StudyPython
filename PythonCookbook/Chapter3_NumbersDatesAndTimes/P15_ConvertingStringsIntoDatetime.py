from datetime import datetime
from datetime import datetime

text = '2012-09-21'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)
print(y)