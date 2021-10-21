'''
Date and Time
Author: Shuvo Kumar Shill
Date: 21.10.2021
------------------------
date clase
time class
datetime calss
timedelta calss
'''
from datetime import date, datetime
dtobj = datetime.now()
print(dtobj)

dtobj2 = date.today()
print(dtobj2)

print(dtobj.year)
print(dtobj.month)
print(dtobj.day)

print(dtobj.hour)
print(dtobj.second)
print(dtobj.microsecond)

print(dtobj.strftime('week Day short : %a'))
print(dtobj.strftime('week Day long : %A'))
print(dtobj.strftime('week Day Number : %w'))

print(dtobj.strftime('Month short : %b'))
print(dtobj.strftime('Month Long : %B'))
print(dtobj.strftime('Month Number : %m'))

print(dtobj.strftime('Day of month : %d'))
print(dtobj.strftime('Year without century : %y'))
print(dtobj.strftime('Year with century : %Y'))

print(dtobj.strftime('Full time 0-23 : %T'))
print(dtobj.strftime('Full date : %D'))

print(dtobj.strftime('Hour 0-23 : %H'))
print(dtobj.strftime('Hour 0-12 : %I'))
print(dtobj.strftime('AM/PM : %p'))
print(dtobj.strftime('Minute : %M'))
print(dtobj.strftime('Second : %S'))
print(dtobj.strftime('Micro-Second : %f'))


# Display custom formate
print('Display custom format : ')
print("+"*40)
#21-10-2021 
print(dtobj.strftime('%d-%m-%Y'))
print(dtobj.strftime('%d.%m.%Y'))
print(dtobj.strftime('%A, %d.%m.%Y'))


print(dtobj.strftime('%I:%M:%S %p'))
print(dtobj.strftime('%H:%M:%S '))

