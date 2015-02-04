# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 18:53:13 2015

@author: liuweizhi
"""

## version 1
n=input();s=sorted(raw_input());k=list(set(s))
c=[s.count(i) for i in k]
b=any([i%n!=0 for i in c])
if b:
    print -1
else:
    d=[i/n for i in c]
    ans=[k[i]*d[i] for i in range(len(d))]
    print n*''.join(ans)
        

