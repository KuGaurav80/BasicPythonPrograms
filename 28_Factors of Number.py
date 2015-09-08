# python_factor of number.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

def print_factors(x):

   print 'The factors of {0} are: '.format(x)
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input("Enter a number: "))

print_factors(num)