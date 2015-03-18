# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 19:42:09 2015

@author: liuweizhi
"""

## version 1
print map(lambda x:len([foo for foo in range(1,x[4]+1) if (foo%x[0]==0) or (foo%x[1]==0) or (foo%x[2]==0) or (foo%x[3]==0)]), [[input() for _ in range(5)]])[0]

## version 2
I=input;x=map(I,' '*4);print sum(any(i%j<1for j in x)for i in range(-I(),0))