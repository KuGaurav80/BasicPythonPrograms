# python_Matrix Multiplication.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

X = [[23,71,13],
    [43,54,65],
    [17,83,29]]
# 3x4 matrix
Y = [[52,18,41,0],
    [16,47,33,10],
    [6,5,4,12]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j]= X[i][k]*Y[k][j]

for r in result:
    print r