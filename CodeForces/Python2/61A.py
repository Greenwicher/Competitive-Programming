# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 21:11:13 2015

@author: liuweizhi
"""

## version 1
a=raw_input();b=raw_input()
c=bin(int(a,2)^int(b,2)).replace('0b','')
print '0'*(len(a)-len(c))+c

## version 2
a=raw_input();b=raw_input();c=''
for i in range(len(a)):
    if a[i]==b[i]:
        c+='0'
    else:
        c+='1'
print c

## version 3 (zip())
print ''.join("10"[i==j]for i,j in zip(raw_input(),raw_input()))

## version 4 (按位异或)
print''.join([str(int(a)^int(b))for a,b in zip(raw_input(),raw_input())])