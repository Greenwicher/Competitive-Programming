# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:55:59 2015

@author: liuweizhi
"""

## version 1
'''
The main point of this problem is to transform
the condition |b_{i,c}-b_{j,c}|<=1 for all i,j
given c into max|b_{i,c}-b_{j,c}|<=1 which is 
equivalent to max{b_{i,c}}-min{b_{i,c}}<=1. Without
loss of generality, suppose the number of pebble
of each color from smallest pile is the smallest, and 
that from largest pile is the largest. Then we only
need to concern how to construct the smallest 
pile and largest pile since other piles will 
automatically satisfy the absolute difference
condition. Finally, a periodic sequence with 
largest length min(a)+k (this value is the largest 
length of the array a, otherwise, such construction
could not be found) is constructed (array c
below ) to construct all the other color sequence
of all piles.
'''
I=lambda:map(int,raw_input().split())
n,k=I();a=I();c=[i%k+1 for i in range(min(a)+k)]
if min(a)+k<max(a):
    print 'NO'
else:
    print 'YES'
    for i in range(n):
        print ' '.join(map(str,c[:a[i]]))