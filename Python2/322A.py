# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 16:10:43 2015

@author: liuweizhi
"""

## version 1
n,m=map(int,raw_input().split())
print n+m-1
for i in range(max(n,m)):
    if n<m:
        print 1,i+1
    else:
        print i+1,1
for i in range(min(n,m)-1):
    print i+2,i+2
    
## version 2
a,b=map(int,raw_input().split())
print a+b-1
for i in range(1,a+b):print max(1,i-b+1),min(i,b)