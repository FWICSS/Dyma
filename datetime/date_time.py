#  Copyright (c) 2022. Code by Dimitri AIGLE
from datetime import datetime, time, date

a =datetime(1850, 5, 1)
print(a)

b = datetime.today()
print(b)

c = datetime.now()
print(c)

une_date = datetime.now()

print(une_date.year)  #  2021
print(une_date.month)  # 12
print(une_date.day)  # 11
print(une_date.hour)  # 16
print(une_date.minute)  # 6
print(une_date.second)  # 8
print(une_date.microsecond)  # 941860


temps = time(12, 23, 30)
une_date = date(2021, 6, 15)

print(datetime.combine(une_date, temps))
# 2021-06-15 12:23:30