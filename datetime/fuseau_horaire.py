#  Copyright (c) 2022. Code by Dimitri AIGLE
from datetime import datetime, time, date
from dateutil import tz

m = datetime.today()
print(m)

n = datetime.now(tz.gettz('GP'))
print(n)
print(n.dst())
print(n.tzinfo)
print(n.tzname())