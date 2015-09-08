# python_sum of natural numbers.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

num = int(input("Enter a number: "))

if num < 0:
   print("Enter +ve number")
else:
   sum = 0
   # use while loop to iterate un till zero
   while(num > 0):
       sum += num
       num -= 1
   print "The sum is {0}".format(sum)