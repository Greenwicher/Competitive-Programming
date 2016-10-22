# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:28:29 2015

@author: liuweizhi
"""

## version 1
old=[];new=[]
for i in range(int(input())):
    o,n=input().split()
    if o in new:
        new[new.index(o)]=n
    else:
        old.append(o)
        new.append(n)
print(len(old))
for i in range(len(old)):
    print(old[i],new[i])

## version 2
n,h=int(input()),{}
for i in range(n):
	o,n=input().split()
	h[n]=h.get(o,o)
	h.pop(o,None)
print(len(h))
for n,o in h.items():
	print(o,n)

## version 3
h = {}
for i in range(int(input())):
    h1, h2 = input().split()
    if h1 in h:
        h[h2] = h[h1]
        del h[h1]
    else:
        h[h2] = h1
print(len(h))
for k in h:
    print(h[k], k)
        