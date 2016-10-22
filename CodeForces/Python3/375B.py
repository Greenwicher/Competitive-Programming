# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 18:24:13 2016

@author: liuweizhi
"""

#%% Version 1
n,word = input(),input()
# simplify open-closing pairs
word = word.replace('(','|').replace(')','|').split('|')
# check whether the first item in word is within parenthesis
flag = word[0]=='('
a,b = 0,0
# the length of the longest word outside the parentheses
for foo in word[[0,1][flag]::2]:
    a = max(a,*[len(w) for w in foo.split('_')])
# the number of words inside the parentheses    
for foo in word[[1,0][flag]::2]:
    b += len([w for w in foo.split('_') if w])
print(a,b)