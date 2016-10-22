# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:04:31 2015

@author: liuweizhi
"""

## version 1
import math
r,x,y,a,b=map(int,raw_input().split())
d=((x-a)**2+(y-b)**2)**(0.5)
print int(math.ceil(d/(2*r)))

## version 2
r,x,y,x1,y1=map(int,raw_input().split())
d=(((x1-x)**2)+((y1-y)**2))**0.5
print int(d/(2*r))+(d%(2*r)!=0)