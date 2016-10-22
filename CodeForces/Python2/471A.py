# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 17:36:00 2015

@author: liuweizhi
"""

## version 1
seq=map(int,raw_input().split())
num=set([seq.count(i) for i in set(seq)])
if num==set([6]) or num==set([4,2]):
    print 'Elephant'
elif num==set([5,1]) or num==set([4,1,1]):
    print 'Bear'
else:
    print 'Alien'
    
## version 2
l = map(int, raw_input().split())
l = sum([l.count(i)**2 for i in l])
print "Elephant" if l%72==0 else "Bear" if l>60 else "Alien"

## version 3
l = map(int, raw_input().split())
l = sum([l.count(i)**2 for i in l])
print "Elephant" if l%72==0 else "Bear" if l==66 or l==126 else "Alien"

## version 4
from itertools import *
a=sorted([len(list(x[1])) for x in groupby(sorted(raw_input().split()))])
print 'Alien' if a[-1]<4 else 'Bear' if a[0]==1 else 'Elephant'

## version 5
l = map(int,raw_input().split())
m = sorted([l.count(x) for x in set(l)])
if m[-1] < 4:
    print "Alien"
elif m[0] == 1: 
    print "Bear"
else:
    print "Elephant"