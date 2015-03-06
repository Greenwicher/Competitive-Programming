# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:19:04 2015

@author: liuweizhi
"""

## version 1
s,t=raw_input(),raw_input();k=-1
f=lambda x:''.join(sorted(x))
for i in t:
    if s[k+1:].find(i)!=-1:
        k=s[k+1:].find(i)+k+1
    else:
        k=-1;break
print [[['need tree','both'][f(t) in f(s)],'array'][f(t)==f(s)],'automaton'][k!=-1]