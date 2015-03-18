# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 15:30:57 2015

@author: liuweizhi
"""

## version 1
s=raw_input();k=input();w=map(int,raw_input().split())
print sum([w[ord(s[i])-ord('a')]*(i+1) for i in range(len(s))])+sum(range(len(s)+1,len(s)+1+k))*max(w)