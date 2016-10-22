# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 12:52:27 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
s,n=I();seq=[]
for i in range(n):
    seq.append(I())
seq=sorted(seq)
i=0;
while i<=n-1 and s>seq[i][0]: s+=seq[i][1]; i+=1;
print ['NO','YES'][i>n-1] 

## version 2
I=lambda:map(int,raw_input().split())
s,n=I();i=0;
seq=sorted([I() for _ in range(n)])
while i<=n-1 and s>seq[i][0]: s+=seq[i][1]; i+=1;
print ['NO','YES'][i>n-1] 

## version 3
I=lambda:map(int,raw_input().split())
s,n=I()
for x,y in sorted(I()for z in[0]*n):s=(s+y)*(x<s)
print"YNEOS"[s==0::2]