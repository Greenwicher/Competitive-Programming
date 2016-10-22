# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 12:41:45 2015

@author: liuweizhi
"""

## version 1 (apparently too slow)
f=lambda n:(1+2**n+3**n+4**n)%5
print f(input())

## version 2
n=input()
print (1+[2,4,8,6][n%4-1]+[3,9,7,1][n%4-1]+[4,6][n%2-1])%5

## version 3
print(input()%4<1)*4