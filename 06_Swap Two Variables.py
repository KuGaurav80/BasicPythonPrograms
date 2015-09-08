# python_swap two variables.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

num1= input("Enter first variable: ")
num2= input("Enter 2nd variable: ")

temp= num1
num1= num2
num2= temp

print 'values after swapping: {0} , {1}'.format(num1,num2)