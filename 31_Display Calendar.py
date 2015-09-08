# python_Calendar.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

import calendar

# ask of month and year
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy,mm))