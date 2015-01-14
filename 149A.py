# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 22:39:05 2015

@author: liuweizhi
"""

## version 1
k=input();seq=sorted(map(int,raw_input().split()));
m=0;b=0;
while b<k and seq: b+=seq[-1]; seq.pop(); m+=1
print m*(b>=k)-1*(b<k) 


## version 2
n=input();s=[0]+sorted(map(int,raw_input().split()))
while n*s:n-=s.pop()
print-len(s)%14-1