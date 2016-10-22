# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 18:27:34 2015

@author: liuweizhi
"""

## version 1
import math
n = input()
# calculate the row number of n, row starts from 1
row = int(math.ceil(math.log(n/5.0+1)/math.log(2)-1))+1
# calculate the column group of n
column = (n-5*(2**(row-1)-1))/(-2**(row-1))*(-1)
print ['', 'Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard'][column]

## version 2
n=input()-1
while n>4:n=n-5>>1
print"SLPRHheeaoeonjwlnneadaysror\nhdnd"[n::5]

## version 3
n=input()-1
while n>=5:
	n=(n-5)/2
print "SLPRHheeaoeonjwlnneadaysror\nhdnd\n\n\n"[n::5]