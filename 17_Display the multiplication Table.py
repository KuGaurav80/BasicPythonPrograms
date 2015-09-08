# python_Display the multiplication Table.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

num = int(input("Display multiplication table of? "))

for i in range(1,11):
   print '{0}x{1}={2}'.format(num,i,num*i)