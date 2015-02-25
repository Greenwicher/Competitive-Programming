# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 11:00:15 2015

@author: liuweizhi
"""

## version 1
a=input()
for i in range(a+1,a+100):
    if '8' in str(i):
        print i-a
        break

## version 2
n=input()
c=1
while '8' not in str(n+c):
    c+=1
print c
