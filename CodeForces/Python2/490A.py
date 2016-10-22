# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 13:06:59 2015

@author: liuweizhi
"""

## version 1
input()
t=map(int,raw_input().split())
f=lambda i,t:[j+1 for j in range(len(t)) if t[j]==i]
a=f(1,t);b=f(2,t);c=f(3,t)
teams=min([len(a),len(b),len(c)])
print teams
for i in range(teams):
    print a[i],b[i],c[i]
    
## version 2
input()
X=[[],[],[]]
for i,s in enumerate(raw_input().split()):X[int(s)-1].append(i+1)
print min(map(len,X))
while all(X):print X[0].pop(),X[1].pop(),X[2].pop()