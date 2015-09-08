# python_fibonacci-recursion.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_recursion(n-1) + fibonacci_recursion(n-2))

terms= int(input('Enter no. of terms: '))
if terms <= 0:
    print 'enter only +ve int.'
else:
    print 'fibonacci-sequence: '
    for i in range(terms):
        print fibonacci_recursion(i)