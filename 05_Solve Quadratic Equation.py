# python_quadratic equation.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

import cmath # complex math

a= float(input('Enter a: '))
b= float(input('Enter b: '))
c= float(input('Enter c: '))

d= (b**2)-(4*a*c)

s1= (-b-cmath.sqrt(d))/(2*a)
s2= (-b+cmath.sqrt(d))/(2*a)

print 'Answers: {0},{1}'.format(s1,s2)