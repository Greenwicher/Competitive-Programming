# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 13:07:23 2015

@author: liuweizhi
"""

## version 1
n = input()
s = map(int, raw_input().split())
num = [0,0,0,0]
for i in s:
    num[i-1] += 1
ans = 0
a4 = num[3]
a31 = min(num[2], num[0])
num[2] = num[2] - a31
a3 = num[2]
num[0] = num[0] - a31
a22 = num[1]/2
num[1] = num[1] - a22*2
a211 = min(num[1], num[0]/2)
num[1] = num[1] - a211
num[0] = num[0] - a211*2
a21 = min(num[1], num[0])
num[1] = num[1] - a21
num[0] = num[0] - a21
a2 = num[1]
a1a = (num[0] / -4) * (-1)

print a4+a31+a3+a22+a211+a21+a2+a1a


# version 2
n=int(raw_input())
a=map(map(int,raw_input().split()).count,range(1,5))
print a[3] + a[2] + (a[1] * 2 + max(a[0]-a[2], 0) + 3)/ 4