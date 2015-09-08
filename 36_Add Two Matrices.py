# python_add two matrices.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

X= [[1,71,3],
    [12,1,13],
    [21,5,32]]

Y= [[11,17,13],
    [21,1,3],
    [12,51,23]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(X)):
    for j in range(len(Y)):
        result[i][j]= X[i][j] + Y[i][j]

for r in result:
    print r