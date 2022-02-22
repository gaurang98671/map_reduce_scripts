#! /usr/bin/python3 -O
import ast
import sys
d = {}

#mapA = ast.literal_eval(input())
#mapB = ast.literal_eval(input())

for i in sys.stdin:
    
    lit = i.strip().split(' / ')
    if lit[0] == "/":
        break
    #lit = ast.literal_eval(i)
    lit[0] = ast.literal_eval(lit[0])
    lit[1] = ast.literal_eval(lit[1])
    a = (lit[0], lit[1][1])
    if a in d:
        d[a] *= int(lit[1][2])
    else:
        d[a] = int((lit[1][2]))
for i in sys.stdin:
    lit = i.strip().split(' / ')
    lit[0] = ast.literal_eval(lit[0])
    lit[1] = ast.literal_eval(lit[1])
    a = (lit[0], lit[1][1])
    if a in d:
        d[a] *= int(lit[1][2])
    else:
        d[a] = int((lit[1][2]))
d2 = {}

for i in d:
    a = i[0]
    if a in d2:
        d2[a] += d[i]
    else:
        d2[a] = d[i]

for i in d2:
    print(i, d2[i])


