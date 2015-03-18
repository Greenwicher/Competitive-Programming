# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 14:31:39 2015

@author: liuweizhi
"""

## version 1
n=input();flag=True
b=[[120 for i in range(n+2)] for i in range(n+2)]
for i in range(n):
    b[i+1][1:n+1]=map(ord,raw_input())
for i in range(n):
    for j in range(n):
        if [b[i][j+1],b[i+2][j+1],b[i+1][j],b[i+1][j+2]].count(111)%2!=0:
            flag=False
            break
print ['NO','YES'][flag]

## version 2
n=input()
b=['x'*(n+2)]
b+=['x'+raw_input()+'x' for i in range(n)]
b+=['x'*(n+2)]
print 'YES' if all(not reduce(lambda x,y:x^y,(b[x/n+1+i][x%n+1+j]=='o' for (i, j) in zip((-1,0,0,1),(0,-1,1,0)))) for x in range(n*n)) else 'NO'

## version 3
n = input()
dice = ['x'*(n+2)] + ['x'+raw_input()+'x' for i in range(n)] + ['x'*(n+2)]
print 'NO' if sum([sum([((dice[i-1][j]=='o')+(dice[i+1][j]=='o')+(dice[i][j-1]=='o')+(dice[i][j+1]=='o'))%2 for j in range(1, n+1)]) for i in range(1, n+1)]) else 'YES'