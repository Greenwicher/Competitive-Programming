# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 14:00:38 2015

@author: liuweizhi
"""

## version 1
s,t=raw_input(),raw_input()
i=j=0
while j<len(t): i+=1*(s[i]==t[j]);j+=1
print i+1

## version 2
r=raw_input
a=r()
i=0
for c in r():i+=a[i]==c
print-~i