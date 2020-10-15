# Calendar module exploration
import calendar

# get a text-based calendar object, starting on Sunday:
tc = calendar.TextCalendar(calendar.SUNDAY)

print("JUST OCTOBER:\n")
tc.prmonth(2020, 10)

print("\nTHE WHOLE YEAR:\n")

for month in range(1, 13):
    tc.prmonth(2020, month)  # print all 12 months of 2020
    
''' 
ASSIGNMENT:
1. Write code to ask the user for a year and give them all the months calendars
for that year (this will only take one added line before the for loop and 
then just alter the for loop to use that year)
(when you test it out, try some crazy years too...)
  

2. Then write code that would show all the months for a user-chosen year, 
but will start the calendar on a day other than Sunday (see line 5 above)
'''
