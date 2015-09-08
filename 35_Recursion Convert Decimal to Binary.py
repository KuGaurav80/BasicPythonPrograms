# python_decimal number into binary number using recursive function.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

def binary(n):
    if n >1:
        binary(n/2)
    print n%2,
dec= int(input('enter digit: '))
binary(dec)