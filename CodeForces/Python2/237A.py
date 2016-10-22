# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 21:00:00 2015

@author: liuweizhi
"""

## version 1
seq=[raw_input() for _ in range(input())]
print max([len(p) for p in ''.join([str(int(i==j)) for i,j in zip(seq[:len(seq)-1],seq[1:])]).split('0')])+1

## version 2 (usage of dict)
x={}
for _ in range(input()):
  s=raw_input()
  x[s]=x.get(s,0)+1
print max(x.values())