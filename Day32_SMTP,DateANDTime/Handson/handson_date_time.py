import datetime

c = datetime.datetime.now() #now is a method of datetime class which is in datetime module
# datetime.datetime.now() will give us the current date and time in the form of a datetime object
print(c)
print(type(c))
print(c.year)
print(c.month)
print(c.day)
print(c.hour)
print(c.minute)
print(c.second)
week = c.weekday()
print(week) #0 is for Monday and 6 is for Sunday

date_of_birth = datetime.date(1998, 9, 24,hour=4) # works with year, month, day,hours and sec
print(date_of_birth)
print(type(date_of_birth))