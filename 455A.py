# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 11:09:40 2015

@author: liuweizhi
"""

## version 1 (wrong answer)
n=input();a=sorted(map(int,raw_input().split()))
b=[[i,a.count(i)] for i in set(a)]
f=lambda b,k: sum([p[0]*p[1] for p in b[k::2]])
print max(f(b,0),f(b,1))


## version 2 (wrong answer)
n=input()
a=sorted(map(int,raw_input().split()))
b=[[i,a.count(i)] for i in set(a)]
d=[0 for i in range(len(b)+1)]
k=[0 for i in range(len(b)+1)]
for i in range(1,len(b)+1):
    d[i]=[d[i-1]+b[i-1][0]*b[i-1][1],d[i-1]][(b[i-1][0]==b[i-2][0]+1)and(k[i-1]==b[i-2][0])]
    k[i]=[b[i-1][0],k[i-1]][(b[i-1][0]==b[i-2][0]+1)and(k[i-1]==b[i-2][0])]
print d[-1]

## version 3 (Time limit exceeded on test 11)
n=input()
a=sorted(map(int,raw_input().split()))
b=[[0,0],[0,0]]+[[i,a.count(i)] for i in set(a)]
m=len(b)
d=[0 for i in range(m)]
k=[0 for i in range(m)]
for i in range(2,m):
    d[i]=max(d[i-2]+b[i][0]*b[i][1],d[i-1]+b[i][0]*b[i][1]*(1-((b[i][0]==b[i-1][0]+1)and(k[i-1]==b[i-1][0]))))
    k[i]=[b[i][0],k[i-1]][(b[i][0]==b[i-1][0]+1)and(k[i-1]==b[i-1][0])and(d[i-1]>d[i-2]+b[i][0]*b[i][1])]
print d[-1]

## version 3.1
n=input();a={}
for i in map(int,raw_input().split()):
    if i in a:
        a[i]+=1
    else:
        a[i]=1
b=sorted([[0,0],[0,0]]+[[i,a[i]] for i in a])
m=len(b)
d=[0 for i in range(m)]
k=[0 for i in range(m)]
for i in range(2,m):
    d[i]=max(d[i-2]+b[i][0]*b[i][1],d[i-1]+b[i][0]*b[i][1]*(1-((b[i][0]==b[i-1][0]+1)and(k[i-1]==b[i-1][0]))))
    k[i]=[b[i][0],k[i-1]][(b[i][0]==b[i-1][0]+1)and(k[i-1]==b[i-1][0])and(d[i-1]>d[i-2]+b[i][0]*b[i][1])]
print d[-1]

## version 4 (large space for short time)
n=input()
a=[0 for _ in range(10**5+1)]
for i in map(int,raw_input().split()):
    a[i]+=1
d=[0 for _ in range(10**5+1)]
d[1]=a[1]
for i in range(2,10**5+1):
    d[i]=max(d[i-2]+a[i]*i,d[i-1])
print d[-1]

## version 5 (reduce space than version 4)
n, b = input(), [0]*10**6
for a in map(int,raw_input().split()):
	b[a] += 1
for i in xrange(2,10**6):
	b[i] = max(b[i-1], b[i]*i+b[i-2])
print b[-1]