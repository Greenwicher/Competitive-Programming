# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 11:11:51 2015

@author: liuweizhi
"""

## version 1
s=[raw_input() for i in range(4)]
for i in range(3):
    for j in range(3):
        o=[s[i][j],s[i][j+1],s[i+1][j],s[i+1][j+1]]
        if (o.count('.')>2 or o.count('#')>2):
            print 'YES'
            exit()
print 'NO'