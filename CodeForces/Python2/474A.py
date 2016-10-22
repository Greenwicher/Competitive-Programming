# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 20:48:48 2015

@author: liuweizhi
"""

## version 1
board='qwertyuiopasdfghjkl;zxcvbnm,./'
i=2*(raw_input()!='R')-1
word=raw_input()
ans=''
for foo in word:
    ans+=board[board.index(foo)+i]
print ans

## version 2
s = "qwertyuiopasdfghjkl;zxcvbnm,./"
d= -1 if raw_input()=='R' else 1
print ''.join(s[s.find(c)+d] for c in raw_input())