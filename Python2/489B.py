# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 11:27:31 2015

@author: liuweizhi
"""

## version 1
I=lambda x:map(int,raw_input().split()) if x else input()
n=I(0);a=sorted(I(1))
m=I(0);b=sorted(I(1))
a,b=[[a,b],[b,a]][(len(a)>len(b))]
for i in a:
    for j in b:
        if abs(i-j)<=1:
            b.pop(b.index(j))
            break
print max(n,m)-len(b)
    
## version 2
R=lambda:sorted(map(int,raw_input().split()))
n,a,m,b=input(),R(),input(),R()
i=j=ans=0
while i<n and j<m:
	if abs(a[i]-b[j])<=1: ans+=1; i+=1; j+=1
	elif a[i]<b[j]: i+=1
	else: j+=1
print ans
