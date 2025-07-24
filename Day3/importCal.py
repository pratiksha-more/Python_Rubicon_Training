#import Calender module
import calendar
#Display the calendar for a specific month and year
print(calendar.month(2025,8))
#Display the calendar for a specific year--
print(calendar.calendar(2025))
# #Display the current date
from datetime import datetime       
current_date = datetime.now()

print("Current date:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

current_day = current_date.day
current_month = current_date.month
current_year = current_date.year
current_weekday = current_date.strftime("%A")
current_time = current_date.strftime("%H:%M:%S")
print("Current day:", current_day)  
print("Current month:", current_month)
print("Current year:", current_year)
print("Current weekday:", current_weekday)
print("Current time:", current_time)


for i in range(5):
    print(i)

print(len("Python"))