# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:13:49 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
p,q,l,r=I();m=[];n=[];ans=0
for i in range(p):
    a,b=I()
    m+=range(a,b+1)
for i in range(q):
    c,d=I()
    n+=[j+l for j in range(c,d+1)]
for i in range(r-l+1):
   if len(set(m+n))<len(m)+len(n):ans+=1
   n=[j+1 for j in n]
print ans

## version 2
R=lambda:map(int,raw_input().split())
p,q,l,r=R()
a=[R() for _ in range(p)]
b=[R() for _ in range(q)]
t=set()
for x in a:
  for y in b:
    t|=set(range(max(l,x[0]-y[1]),min(r,x[1]-y[0])+1,1))
print len(t)

## version 3
'''
enumerate all the possible case based on comprehension
'''
R=lambda:map(int,raw_input().split())
p,q,l,r=R()
ab,cd=[R()for i in range(p)],[R()for i in range(q)]
print [any(ab[k][1]>=cd[j][0]+i and cd[j][1]+i>=ab[k][0]for k in range(p) for j in range(q)) for i in range(l,r+1)].count(1)

## version 4
'''
use a large array to represent whether each time
are in the interval and derive whether the two 
time schedule share the same time moment by
a sumproduct.
'''
p,q,l,r = map(int,raw_input().split())
ab = [map(int,raw_input().split()) for i in range(p)]
cd = [map(int,raw_input().split()) for i in range(q)]
ans = 0

zon = [0]*2002
for a,b in ab:
    zon[a:b+1] = [1]*(b-a+1)
for t in range(l,r+1):
    xon = [0]*1001
    for c,d in cd:
        xon[c+t:d+t+1] = [1]*(d-c+1)
    ans += min(1,sum([xon[i]*zon[i] for i in range(1001)]))
    
print ans