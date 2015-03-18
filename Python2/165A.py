# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 13:23:12 2015

@author: liuweizhi
"""

## version 1 (Time limit exceeded on test 1)
s=[[0 for _ in range(2002)] for _ in range(2002)]
for _ in range(input()):
    x,y=map(int,raw_input().split())
    s[x+1000][y+1000]=1
c,r=[set(),set()]
for i in range(2002):
    r=r.union([(j,i) for j in range(2002) if s[j][i]==1][1:-1])
    c=c.union([(i,j) for j in range(2002) if s[i][j]==1][1:-1])
print len(r.intersection(c))

## version 2
s=[];ans=0
for _ in range(input()):
    s.append(map(int,raw_input().split()))
for i in range(len(s)):
    r=[s[j][0] for j in range(len(s)) if s[j][1]==s[i][1]]
    c=[s[j][1] for j in range(len(s)) if s[j][0]==s[i][0]]
    ans+=1*(min(r)<s[i][0]<max(r) and min(c)<s[i][1]<max(c))
print ans

## version 3 (set expression and cmp function)
A=[map(int,raw_input().split())for i in[0]*input()]
print sum(len({(cmp(x,X),cmp(y,Y))for x,y in A if x==X or y==Y})>4for X,Y in A)