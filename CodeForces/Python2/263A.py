# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 11:21:57 2015

@author: liuweizhi
"""

## version 1
row = 1
line = raw_input()[::2]
while not ('1' in line):
    line = raw_input()[::2]
    row += 1
column = line.find('1') + 1
print abs(row-3)+abs(column-3)


## version 2 (beautiful initialization for l)
l=[2,1,0,1,2]
for i in l:
 s=raw_input()
 if"1"in s:print i+l[s.find("1")/2]
 
## version 3 (smart use of try and index())
for i in xrange(5):
    try: print abs(i - 2) + abs(raw_input().split().index('1') - 2)
    except: pass

## version 4 (enumerate())
for i in range(5):
  for j, a in enumerate(map(int, raw_input().split())):
    if a == 1:
      print abs(2 - i) + abs(2 - j)