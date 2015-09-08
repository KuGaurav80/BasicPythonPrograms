# python_Find Numbers Divisible by Another Number.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

my_list = [12, 13, 26, 36, 39, 65, 55, 39, 102, 112, 210, 339, 221,]

result = list(filter(lambda x: (x % 13 == 0), my_list))
print "Numbers divisible by 13 are",result