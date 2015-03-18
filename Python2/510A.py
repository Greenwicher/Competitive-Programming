# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 13:07:22 2015

@author: liuweizhi
"""

## version 1
n,m=map(int,raw_input().split())
for i in range(n):
    print ['#'*m,'.'*(m-1)+'#','#'+'.'*(m-1)][(i%2)*(i%4+1)/2]