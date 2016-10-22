# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 12:16:50 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,m=I();seq=I();group=1
for i in range(1,len(seq)):
    if seq[i]<seq[i-1]:
        group+=1        
print (group-1)*n+seq[-1]-1

## version 2 (圆圈循环步数计算)
I=lambda:map(int,raw_input().split())
n,m=I()
p=r=1
for v in I():r+=(v-p)%n;p=v
print~-r

## version 3 (zip())
r=lambda:map(int, raw_input().split())
n,m=r()
N=r()
print sum(p>n for p,n in zip(N, N[1:]))*n + N[-1] - 1