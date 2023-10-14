#  Copyright (c) 2022. Code by Dimitri AIGLE
from datetime import time,date,datetime

import locale

locale.setlocale(locale.LC_TIME,"fr")
h = date.fromtimestamp(1666999304)
print(h.strftime("%A %d %B %Y"))