# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 11:01:10 2015

@author: liuweizhi
"""

## version 1
g=lambda x:2*x+x*(x+1)*(x-2)/2-(x-1)*x*(2*x-1)/6
print g(input())

## version 2
n=input();print n*(n**2+5)/6