# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 17:52:49 2015

@author: liuweizhi
"""

## version 1
word1 = raw_input().lower()
word2 = raw_input().lower()
if word1<word2:
    print '-1'
elif word1==word2:
    print '0'
else:
    print '1'
    
## version 2
print cmp(*[raw_input().lower()for x in' '*2])