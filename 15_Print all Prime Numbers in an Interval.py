# python_Print all Prime Numbers in an Interval.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

l= int(input('enter lower limit: '))
u= int(input('enter upper limit: '))

for num in range(l,u+1):
   if all(num%i!=0 for i in range(2,num)):
       print num
