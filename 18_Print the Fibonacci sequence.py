# python_Fibonacci.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'
terms= int(input('enter the No. of terms: '))

n1= 0
n2= 1
count= 2
if terms <= 0:
    print 'only +ve int.'
elif terms == 1:
    print 'Fibonacci sequence: {0}'.format(n1)
else:
    print'Fibonacci sequence: '
    print n1,', ',n2,', ',
    while count < terms:
        n= n1+n2
        print n,', ',
        n1= n2
        n2= n
        count +=1

