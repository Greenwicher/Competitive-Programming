# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 17:44:42 2015

@author: liuweizhi
"""

## version 1
word=raw_input()
upper=sum(foo.isupper() for foo in word)
print [word.lower(),word.upper()][2*upper>len(word)]

## version 2 (map())
s=raw_input()
print[s.lower(),s.upper()][sum(map(str.isupper,s))>len(s)/2]

## version 3 (select function based on condition)
s=raw_input()
print [str.upper,str.lower][sum(i.islower() for i in s)*2>=len(s)](s)