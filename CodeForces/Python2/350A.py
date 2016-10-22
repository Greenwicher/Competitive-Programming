# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 12:03:09 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,m=I();a=sorted(I());b=sorted(I())
k=max(max(a),2*a[0])
print [k,-1][k>=b[0]]