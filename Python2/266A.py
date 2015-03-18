# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 18:52:33 2015

@author: liuweizhi
"""

## version 1
n = input()
colors = raw_input()
previous = colors[0]
ans = 0
for foo in colors[1:]:
    if foo==previous:
        ans += 1
    else:
        previous = foo
print ans
     
## version 2
input()
c=raw_input()
print sum(p==n for p,n in zip(c[1:],c))

## version 3
n , s = input() , raw_input()
print sum(s[i]==s[i+1] for i in range(n-1))