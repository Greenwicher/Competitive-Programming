# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 19:59:52 2016

@author: liuweizhi
"""

#%% version 1
words = input().replace(';',',').split(',')
a,b = [],[]
for foo in words:
    if (foo.isdigit() and (foo=='0' or foo[0]!='0')):
        a.append(foo)
    else:
        b.append(foo)
for v in a,b:
    g = ','.join(v)
    print(['"'+g+'"','-'][g==','*len(v)])