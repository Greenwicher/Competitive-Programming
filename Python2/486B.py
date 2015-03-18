# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:01:50 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
R=set();C=set()
S=[]
m,n=I()
for i in range(m):
    r=I()
    for j in range(n):
        if r[j]==0:
            R.add(i);C.add(j)
        else:
            S.append((i,j))
for p in S:
    if S and (len(R)==m or len(C)==n):
        print 'NO'
        break
    if p[0] in R and p[1] in C:
        print 'NO'
        break
else:
    print 'YES'
    for i in range(m):
        print ' '.join(map(str,[1*(not(i in R or j in C)) for j in range(n)]))