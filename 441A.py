# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 14:05:12 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,v=I();seller=[]
for i in range(n):
    a=I()
    if min(a[1:])<v: seller.append(i)
print len(seller)
for i in seller:
    print i+1,
    
## version 2
In = lambda:map(int,raw_input().split())
n,m = In()
ans = [str(x+1) for x in range(n) if m > min(In()[1:])]
print len(ans)
print ' '.join(ans)