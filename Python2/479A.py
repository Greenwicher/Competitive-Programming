# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 22:32:19 2015

@author: liuweizhi
"""

## version 1
I=input;a,b,c=I(),I(),I()
print max([a+b+c,a+b*c,(a+b)*c,a*b+c,a*(b+c),a*b*c])