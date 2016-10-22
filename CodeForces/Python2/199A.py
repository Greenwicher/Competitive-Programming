# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 21:47:59 2015

@author: liuweizhi
"""

## version 1
n=input();f=[0,1,1];i=3
while f[-1]!=n and n>=2:
    f.append(f[i-1]+f[i-2])
    i+=1
k=f.index(n)
g=lambda a,b,c:' '.join(map(str,[a,b,c]))
print [[g(0,0,0),g(0,0,1)][k>=1],g(f[k-2],f[k-2],f[k-3])][k>=3]

## version 2 (.......)
print 0,0,input()