# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 15:47:30 2015

@author: liuweizhi
"""

## version 1
sum=eval(raw_input().replace(' ','+'))
print [-1,sum/5][sum%5==0 and sum>0]