# python_sum of natural numbers.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

def recursion_sum(n):
    if n <=1:
        return n
    else:
        return recursion_sum(n-1)+n
num= int(input('Enter a number: '))
if num < 0:
    print 'Enter +ve num.'
else:
    print 'the sum is {0}'.format(recursion_sum(num))