# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 15:50:43 2015

@author: liuweizhi
"""

## version 1
n=input();seq=map(int,raw_input().split())
for i in range(n):
    mod=[(seq[i]-seq[j])%2 for j in range(n) if j!=i]
    if all(mod):
        print i+1
        break
    
## version 2
input()
a = [int(x) % 2 for x in raw_input().split()]
print a.index(sum(a) < 2) + 1