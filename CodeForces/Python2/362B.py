# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:27:57 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,m=I();
if m!=0:
    d=sorted(I())
else:
    d=[0]
if 1 in d or n in d:
    print 'NO'
else:
    z=1;k=0
    for i in range(1,m):
        z=[1,z+1][d[i]-d[i-1]==1]
        k=max(k,z)
    print 'YES' if k<3 else 'NO'

## version 2
'''
The idea of this algorithm is the same as version
1, but more brief based on some funtional programming
tricks.
'''
I=lambda:map(int,raw_input().split())
n,m=I();d=eval(['sorted(I())','[0]'][m==0])
k=max(map(len,''.join(map(str,[(d[i+1]-d[i]==1)*1 for i in range(m-1)])).split('0')))+1
print 'YNEOS'[((d[0]==1) or (d[-1]==n) or (k>2))::2]

## version 3
'''
Instead of sorting the array d, this algorithm
just check whether x-1 and x+1 is both in d
given x is in d.
'''
N, M = map(int, raw_input().split())
d = set(map(int, raw_input().split()) if M > 0 else [])
print "NO" if 1 in d or N in d or [x for x in d if x-1 in d and x+1 in d] else "YES"

## version 4
'''
This algorithm also firstly sort the array d,
but didn't return the largest number of the 
adjacent sequence but to check if there exists
three adjacent number.
'''
N,M = map(int,raw_input().split())
A = sorted(map(int,raw_input().split())) if M else [0]
print 'NO' if A[0] == 1 or A[-1] == N or [i for i in range(2,M) if A[i-2]+2 == A[i]] else 'YES'

