# python_Calculator.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'


def add(x, y):
   """This function adds two numbers"""

   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""

   return x / y

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

c = int(input("Enter choice(1/2/3/4): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if c == 1:
   print '{0} + {1} = {2}'.format(num1,num2,add(num1,num2))

elif c == 2:
   print '{0} - {1} = {2}'.format(num1,num2,subtract(num1,num2))

elif c == 3 :
      print '{0} * {1} = {2}'.format(num1,num2,multiply(num1,num2))

elif c == 4 :
      print '{0} / {1} = {2}'.format(num1,num2,divide(num1,num2))

else:
   print("Invalid input")