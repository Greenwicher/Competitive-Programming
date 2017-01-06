#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 13:55:00 2017

@author: liuweizhi
"""

#%% Version 1: brute force with binary search (TLE)

# read the input
I = lambda: list(map(int, input().split()))
n = I()[0]
d1 = sorted(I())
m = I()[0]
d2 = sorted(I())

# return the number of items that are larger than x in list d
def bisection(d, x):
    l, r = 0, len(d) - 1
    while(l != r):
        m = (l + r) // 2
        if d[m] <= x:
            l = m + 1
        if d[m] > x:
            r = m
    return [0, len(d) - l][d[l] > x]

# enumerate all the possible value of threshold value d
a, b, maxdiff = 0, 0, -1e100
for foo in [0] + d1 + d2:
    i = bisection(d1, foo)
    j = bisection(d2, foo)
    _a, _b = i * 3 + (n - i) * 2, j * 3 + (m - j) * 2
    diff = _a - _b
    if (diff > maxdiff) or (diff == maxdiff and _a > a):
        maxdiff = diff
        a, b = _a, _b

# print the output
print('%d:%d' % (a,b))

#%% Version 2: brute force with two pointers (AC)

# read the input
I = lambda: list(map(int, input().split()))
n = I()[0]
d1 = [0]+sorted(I())
m = I()[0]
d2 = [0]+sorted(I())

# calculate the the number of items that are larger than maxd in list d1 and d2
index1, index2 = {}, {}
index1[0], index2[0] = n, m
i, j = n, m
while (i>=0 and j>=0):
    maxd = max(d1[i], d2[j])
    if not(maxd in index1):
        index1[maxd] = n - i 
    if not(maxd in index2):
        index2[maxd] = m - j 
    if d1[i] == maxd:
        i -= 1
    if d2[j] == maxd:
        j -= 1
while (i>=0):
    if not(d1[i] in index1):
        index1[d1[i]] = n - i
    i -= 1
while (j>=0):
    if not(d2[j] in index2):
        index2[d2[j]] = m - j
    j -= 1                
    
# enumerate all the possible value of threshold value d
a, b, maxdiff = 0, 0, -1e100
for foo in [0] + d1 + d2:
    i = index1[foo]
    j = index2[foo]
    _a, _b = i * 3 + (n - i) * 2, j * 3 + (m - j) * 2
    diff = _a - _b
    if (diff > maxdiff) or (diff == maxdiff and _a > a):
        maxdiff = diff
        a, b = _a, _b

# print the output
print('%d:%d' % (a,b))
