import datetime 

now = datetime.datetime.now()
weekday = now.weekday()
hour = now.hour
weekday = range(0,6)
hour = range(0,23)
print(now)
if weekday > (0,5) and hour > (9,18)