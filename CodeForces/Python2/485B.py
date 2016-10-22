# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 13:54:51 2015

@author: liuweizhi
"""

## version 1
xmax=ymax=-10**9;xmin=ymin=10**9
for _ in range(input()):
    x,y=map(int,raw_input().split())
    xmax=[xmax,x][x>xmax]
    xmin=[xmin,x][x<xmin]
    ymax=[ymax,y][y>ymax]
    ymin=[ymin,y][y<ymin]
print max(xmax-xmin,ymax-ymin)**2

## version 2
x,y=zip(*[map(int,raw_input().split()) for _ in range(input())])
a=max((max(x)-min(x)),(max(y)-min(y)))
print a*a