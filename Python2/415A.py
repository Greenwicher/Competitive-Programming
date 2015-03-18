# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 17:25:02 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,m=I();k=n+1;a=[0 for i in range(n+1)]
for i in I():
    a[i:k]=[i]*(k-i)
    k=min(k,i) 
print ' '.join(map(str,a[1:]))
    
## version 2
n, m = map(int, raw_input().split())
buttons = map(int, raw_input().split())
for i in range(1, n + 1):
	print filter(lambda x: x <= i, buttons)[0],

