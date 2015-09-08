# python_Prime number.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

num= int(input('Enter number: '))
if num>1:
    for i in range(2,num):
        if (num % i)==0:
            print'{0} is not prime number({0} is divisible by {1} )'.format(num,i)
            break
    else:
        print '{0} is prime number'.format(num)
else:
        print '{0} is not prime number'.format(num)