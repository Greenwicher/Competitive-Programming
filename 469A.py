# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 21:48:17 2015

@author: liuweizhi
"""

## version 1
g=lambda:map(int,raw_input().split())[1:]
print ['Oh, my keyboard!','I become the guy.'][input()==len(set(g()+g()))]