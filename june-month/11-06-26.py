# Date and Time module in Python
    # The datetime module in used to work with dates and time in python.

'''
=> get current date and time
=> create custom dates
=> formate date
=> perform date calcualtion
'''

# Importing datetime module:-

import datetime

now = datetime.datetime.now()
print(now)

# current date only
today = datetime.date.today()
print(today)

# custom date
custom = datetime.date(2024, 12, 1)
print(custom)

# Access year, month and day

today = datetime.datetime.today()
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# strftime() is used to formate data and time

now = datetime.datetime.now()

formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted)

# date difference

d1 = datetime.date(2002, 12, 1)
d2 = datetime.date(2026, 6, 11)

difference = d2 - d1
print(difference.days)


# 2. Time module in Python
'''
    - working with system time
    - delays in programme
    - measuring execution time
'''

# import time module

import time

current = time.time()
print(current)
# it returns seconds from January 1 1970.

# Pause programme using sleep()

print("Start Programme")
time.sleep(3)
print("Programme ends after 3 seconds")


# current local time
local = time.localtime()
print(local)


# Froamte time
current = time.strftime("%H:%M:%S")
print(current)


# Measure exicution time
start = time.time()

for i in range(1000000):
    pass

end = time.time()

print("Exicution Time:", end - start)


# Display current Date and Time
from datetime import datetime, timedelta

now = datetime.now()
print(now)

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hours:", now.hour)
print("Minutes:", now.minute)
print("Seconds:", now.second)

# 1. datetime.now()
'''returns current date and time'''

# 2. datetime.date.today()
'''return current date'''

# 3. datetime.today()
'''return current local date and time'''

# 4. datetime.utcnow()
'''return current utc time'''
print(datetime.utcnow())

# 5. strftime()
'''formate date/time into string'''

# 6. strptime()
'''convert date/time string into object'''

date = "2025-6-11"

obj = datetime.strptime(date, "%Y-%m-%d")
print(obj)

# 7. timedelta

today = datetime.now()

future = today + timedelta(days=5)
print(future)

# 8. replace()

now = datetime.now()

new_date = now.replace(year=2030)
print(new_date)

# 9. date()
'''extract date only'''

# 10. time()
'''extract time only'''

# 11. weekday()
'''return weekday number'''

now = datetime.now()
print(now.weekday())


# 12. isoweekday()
'''return readable'''

print(now.isoweekday())


# 13. ctime()
'''return readable date and time'''

print(now.ctime())


# 14. timestamp()
'''return seconds since epoch'''

now = datetime.now()
print(now.timestamp())

# 15. fromtimestamp()
'''return timestamp to datetime'''

s = 174986300
print(datetime.fromtimestamp(s))


# Python Time Module Methods:-----

# 1. time()
# 2. ctime()
# 3. sleep()
# 4. localtime()

# 5. gmtime()
print(time.gmtime())

# 6. strftime()
# 7. strptime()
# 8. mktime()
'''converts time tuple in seconds'''

t = time.localtime()
print(time.mktime(t))

# 9. asctime()
'''return tuple seconds in radbale time'''

t = time.localtime()
print(time.asctime(t))

# 10. pref_counter()
'''major performance of time'''

# 11. process_time()
'''return cpu execution time'''

# 12. monotonic()
'''returns continuously increasing clock'''
print(time.monotonic())
