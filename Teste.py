import datetime

import pandas as pd

dt = datetime.datetime.strptime("2013-1-25", '%Y-%m-%d')
print ('{0}/{1}/{2:02}'.format(dt.month, dt.day, dt.year % 100))