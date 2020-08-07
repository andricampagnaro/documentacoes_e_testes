import time
import datetime
import calendar
### Get the current date and time
>>> datetime.datetime.now()
2018-11-01 20:17:12.964253
### Get just the current time
>>> datetime.datetime.now().time()
2018-11-01 20:19:16.819745
### Freeze the program for a set period of time
>>> time.sleep(secs=5)
### Measure runtime of a python command
>>> start = time.time()
>>> 100 / 5
>>> end = time.time()
>>> print(end - start)
0.000005346