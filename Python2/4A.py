# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:27:44 2013

@author: Greenwicher
http://codeforces.com/problemset/problem/4/A

"""



# version 1
input = int(raw_input())

if(input % 2==0 and input != 2):
    print 'YES'
else:
    print 'NO'

# version 2
w = int(raw_input())
print ['YES', 'NO'][1 - int(w%2==0 and w!=2)]