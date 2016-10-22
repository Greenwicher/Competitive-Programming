# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 16:12:36 2015

@author: liuweizhi
"""

## version 1
a=map(int,raw_input().split())
vec=[a[2]-a[0],a[3]-a[1]]
if not(vec[0]) and vec[1]!=0:
    print ' '.join(map(str,[a[0]+vec[1],a[1],a[2]+vec[1],a[3]]))
elif not(vec[1]) and vec[0]!=0:
    print ' '.join(map(str,[a[0],a[1]+vec[0],a[2],a[3]+vec[0]]))
elif abs(vec[0])==abs(vec[1]):
    print ' '.join(map(str,[a[0],a[3],a[2],a[1]]))
else:
    print -1


        
        