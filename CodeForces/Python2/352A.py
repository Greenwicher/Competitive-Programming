# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 14:21:52 2015

@author: liuweizhi
"""

## version 1 (too slow)
n=input();c=''.join(sorted(raw_input().split())[::-1])
d=int(c)/90;a=c.count('5');b=c.count('0')
g=lambda x:x.count('5')>a or x.count('0')>b or (x.count('5')+x.count('0')<len(x))
while d>=0 and g(str(90*d)):
    print d
    d-=1
print [-1, 90*d][d>=0]

## version 2
n=input();c=''.join(sorted(raw_input().split())[::-1]);i=0
while i<len(c) and int('0'+c[i:])%90!=0: i+=1
print [-1,int('0'+c[i:])][i<len(c)]

## version 3
n=input()
x=raw_input().split().count('0')
y=n-x
print(y/9*9*'5'+'0'*x,-(x<1))[y<9or x<1]

## version 4
n = int(raw_input())
f = raw_input().count('5')
z = n - f
print int('5'*(f - f%9) + '0'*z) if z else -1