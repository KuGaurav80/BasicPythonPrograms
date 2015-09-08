# python_largest number.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3

print "The largest number is {0}".format(largest)