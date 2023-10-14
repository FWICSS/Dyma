#  Copyright (c) 2022. Code by Dimitri AIGLE
from date_time import time

a = time(6, 5, 2, 5)
print(a)


temps = time(hour=22, minute=35, second=50, microsecond=200)

print(temps.isoformat(timespec='hours'))  # 22
print(temps.isoformat(timespec='minutes'))  # 22:35
print(temps.isoformat(timespec='seconds'))  # 22:35:50
print(temps.isoformat(timespec='milliseconds'))  # 22:35:50.000
print(temps.isoformat(timespec='microseconds'))  # 22:35:50.000200

temps = time(hour=22, minute=35, second=50, microsecond=200)

print(temps.isoformat(timespec='hours'))  # 22
print(temps.isoformat(timespec='minutes'))  # 22:35
print(temps.isoformat(timespec='seconds'))  # 22:35:50
print(temps.isoformat(timespec='milliseconds'))  # 22:35:50.000
print(temps.isoformat(timespec='microseconds'))  # 22:35:50.000200

temps = time(hour=22, minute=35, second=50)
temps2 = temps.replace(hour=20, minute=10)

print(temps)  # 22:35:50
print(temps2)  # 20:10:50