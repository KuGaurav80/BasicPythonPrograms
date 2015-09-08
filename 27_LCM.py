# python_lcm.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def lcm(x,y):
    if x>y:
        g=x
    else:
        g=y
    while(True):
        if((g % x ==0) and (g % y==0)):
            lcm=g
            break
        g += 1
    return lcm

print 'L.C.M of {0} and {1} is {2}'.format(num1,num2,lcm(num1,num2))