# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 10:29:59 2015

@author: liuweizhi
"""

## version 1
l,r=raw_input().split('|')
o=raw_input()
a=len(l)+len(r)+len(o)
print ['Impossible',o[:a/2-len(l)]+l+'|'+r+o[a/2-len(l):]][a%2==0 and a/2>=len(l) and a/2>=len(r)]