# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 14:15:41 2015

@author: liuweizhi
"""

## version 1
input();sd=[];seq=map(int,raw_input().split())
while (seq):
    sd.append(max(seq[0],seq[-1]))
    seq=[seq[1:],seq[:len(seq)-1]][seq[0]<seq[-1]]
print sum(sd[::2]),sum(sd[1::2])

## version 2
input()
c=map(int,raw_input().split())
q=0;x=[0,0]
while c:x[q]+=c.pop(-(c[0]<c[-1]));q^=1
print x[0],x[1]