# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:17:05 2015

@author: liuweizhi
"""

## version 1
s=[[0 for i in range(3)] for j in range(3)]
r=[0]*3
for i in range(3):
    s[i]=map(int,raw_input().split())
    r[i]=sum(s[i])
s[0][0]=(r[1]-r[0]+r[2])/2
s[1][1]=(r[2]-r[1]+r[0])/2
s[2][2]=(r[0]+r[1]-r[2])/2
for i in range(3):
    print ' '.join(map(str,s[i]))