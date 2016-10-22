# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 10:56:25 2015

@author: liuweizhi
"""

## version 1
n=input()
print -(-n*n/2)
for i in range(n):
    seq=''
    for j in range(n):
        seq+=['C','.'][(i+j)%2!=0]
    print seq
    
## version 2
n=input()
v="C."*n
print(n*n+1)/2
for i in range(n):print v[i:i+n]
    
## version 3
n = int(input())
print (n * n + 1) / 2
print "\n".join("".join(['C', '.'][(i + j) % 2] for i in range(n)) for j in range(n))