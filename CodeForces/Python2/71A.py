# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 12:38:06 2015

@author: liuweizhi
http://codeforces.com/problemset/problem/71/A
"""

# version 1
n = int(raw_input())
for i in range(n):
    word = raw_input()
    l = len(word)
    print [word, word[0]+str(l-2)+word[l-1]][l>10]

