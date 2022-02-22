#! /usr/bin/python3 -O
import sys
mat = []

mat2 = []

n = int(sys.stdin.readline())
for i in range(n):
    row = sys.stdin.readline().strip().split(' ')
    mat.append(row)

n = int(sys.stdin.readline())
for i in range(n):
    row = sys.stdin.readline().strip().split(' ')
    mat2.append(row)

mapA = []
mapB = []
km = len(mat2[0])
im = len(mat)
jm = len(mat2)
for k in range(km):
    for i in range(im):
        for j in range(jm): 
            mapA.append(((i,k),("A", j, mat[i][j])))


for k in range(km):
    for i in range(im):
        for j in range(jm):
            mapB.append(((i,k), ("B", j, mat2[j][k])))

for i in mapA:
    print(i[0],"/", i[1])
print('/')
for i in mapB:
    print(i[0],"/", i[1])
