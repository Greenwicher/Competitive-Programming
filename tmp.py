# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:27:44 2013

@author: Greenwicher
http://codeforces.com/problemset/problem/1/A

"""
import math

[m, n, a] = raw_input().split(' ')
m = int(m)
n = int(n)
a = float(a)

print int(math.ceil(m/a)*math.ceil(n/a))

