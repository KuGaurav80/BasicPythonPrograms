# python_H.C.F of two input number.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

num1= int(input('Enter first no.: '))
num2= int(input('Enter second no.: '))

def hcf(x,y):
    if x > y:
        s = y
    else:
        s = x
    for i in range(1,s+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
print 'H.C.F of {0} and {1} is {2}'.format(num1,num2,hcf(num1,num2))