# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 16:15:41 2015

@author: liuweizhi
"""

## version 1 （wrong anser）
r,c=map(int,raw_input().split());cake=''
for i in range(r):
    cake+=raw_input()
for i in range(r):
    cake[i:i+c+1]=[cake[i:i+c+1],'o'*c][cake[i:i+c+1].find('S')==-1]
for i in range(c):
    cake[i::c]=[cake[i::c],'o'*c][cake[i::c].find('S')==-1]
print cake.count('o')

## version 2
r,c=map(int,raw_input().split());cake=[]
for i in range(r):
    for j in raw_input():
        cake.append(ord(j))
for i in range(r):
    cake[i*c:(i+1)*c]=[cake[i*c:(i+1)*c],[99]*c][83 not in cake[i*c:(i+1)*c]]
for i in range(c):
    cake[i::c]=[cake[i::c],[99]*r][83 not in cake[i::c]]
print sum(1 for i in cake if i==99)
