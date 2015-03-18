# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 18:44:24 2015

@author: liuweizhi
"""

## version 1
input();seq=map(int,raw_input().split())
pol=0;cri=0
for i in seq:
    if i>0:
        pol+=i
    else:
        cri-=min(pol+i,0)
        pol-=min(-i,pol)
print cri


## version 2
