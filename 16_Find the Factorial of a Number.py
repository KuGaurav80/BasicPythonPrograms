# python_Factorial.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

num= int(input('Enter the number: '))
fact=1
if num < 0:
    print 'factorial is not for -ve numbers'
elif num == 0:
    print 'Factorial of 0 is 1 '
else:
    for i in range(1,num+1):
        fact*= i
    print 'Factorial of {0} is {1}'.format(num,fact)