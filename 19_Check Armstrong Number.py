# python_armstrong-number.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

num= int(input('Enter a number: '))
sum= 0
temp= num
while temp > 0:
    digit= temp % 10
    sum += digit ** 3
    temp /=10
if num == sum:
    print "number is Armstrong"
else:
    print 'number is not Armstrong'