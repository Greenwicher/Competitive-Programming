# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 15:05:34 2015

@author: liuweizhi
"""

## version 1 (Time limit exceeded on test 11)
I=lambda:map(int,raw_input().split())
n,m=I();a=[0]+I();b=[0]*(n+2)
for i in range(n+1)[::-1]:
    b[i]=[1,0][a[i] in a[i+1:n+1]]+b[i+1]
for i in range(m):
    print b[input()]

## version 2 (Time limit exceeded on test 11)
I=lambda:map(int,raw_input().split())
n,m=I();a=[0]+I();b=[0]*(n+2);c=[]
for i in range(n+1)[::-1]:
    b[i]=[1,0][a[i] in c]+b[i+1]
    if not(a[i] in c):
        c.append(a[i])
for i in range(m):
    print b[input()]
    
## version 3
I=lambda:map(int,raw_input().split())
n,m=I();a=[0]+I();b=[0]*(n+2);c=[0]*(10**5+1)
for i in range(n+1)[::-1]:
    b[i]=[1,0][c[a[i]]]+b[i+1]
    c[a[i]]=1
for i in range(m):
    print b[input()]
    
## version 4
R=lambda:map(int,raw_input().split())
n,m=R()
a=R()
c=[]
t={}
while a:
  t[a.pop()]=1
  c+=[len(t)]
for _ in range(m):
  print c[n-input()]
  
## version 5
I=lambda:map(int,raw_input().split())
n,m=I()
a=I()
c=[0]*n
d=set()
for i in range(n)[::-1]:
    d.add(a[i])
    c[i]=len(d)
for i in range(m):
    print c[I()[0]-1]