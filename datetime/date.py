#  Copyright (c) 2022. Code by Dimitri AIGLE
from date_time import date

d =  date(1920,2,1)
print(d)

e = date.today()
print(e)

f = date.fromisoformat("2200-01-01")
print(f)

g = date.fromordinal(700000)
print(g)

#timestamp en seconde
h = date.fromtimestamp(1666999304)
print(h)

# anné num semaine num jour semaine
print(h.isocalendar())

#jour de la semaine
print(h.isoweekday())

print(h.strftime("%A %d %B %Y"))