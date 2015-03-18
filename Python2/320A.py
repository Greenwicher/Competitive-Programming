# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 17:11:39 2015

@author: liuweizhi
"""

## version 1
a=raw_input()
for i in map(str,[0,2,3,5,6,7,8,9]):
    if i in a:
        print 'NO'
        exit()
i=0;k=1
while a and k:
    if a[:3]=='144':
        a=a[3:]
    elif a[:2]=='14':
        a=a[2:]
    elif a[:1]=='1':
        a=a[1:]
    else:
        k=0
print ['NO','YES'][k]

## version 2
f=lambda x,b:[y  for z in x for y in z.split(b)]
print ['NO','YES'][''.join(f(f(f([raw_input()],'144'),'14'),'1'))=='']     

## version 3
import re
print 'YES' if re.match("(1|14|144)+$", raw_input()) else 'NO'

## version 4
a=raw_input()

if a.count('1')+a.count('4')!=len(a) or a[0]=='4' or '444' in a:
	print 'NO'
else:
	print 'YES'
 
## version 5
r=raw_input()
for s in "144","14","1":r=r.replace(s,"z")
print"YES"if set(r)<={"z"}else"NO"

## version 6
print 'YNEOS'[set(raw_input().replace('144','*').replace('14','*').replace('1', '*'))!=set('*')::2]