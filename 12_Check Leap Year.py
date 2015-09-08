# python_Leap year.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

year= int(input('Enter year: '))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print '{0} is leap year'.format(year)
else:
    print "{0} is'nt leap year".format(year)
