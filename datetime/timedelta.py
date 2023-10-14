#  Copyright (c) 2022. Code by Dimitri AIGLE
from datetime import time,date,datetime,timedelta
from dateutil import tz, parser
import locale

locale.setlocale(locale.LC_TIME,"fr")

p = datetime.now(tz.UTC)

q = parser.parse("2022-10-28 21:33:37.333435")
print(q)

s = datetime.now()

r =  timedelta(157)
print(r)

t = s + r
print(t)
print(t.strftime("%A"))
print(t>s)

