# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 21:13:00 2015

@author: liuweizhi
"""

## version 1 (wrong answer, the question actually ask to buy only one unit sugar)
I=lambda:map(int,raw_input().split())
n,s=I();ans=-1
f=lambda x:[(s*100-i*x)%100 for i in range(1,int(s*100/x)+1)]+[-1]
for i in range(n):
    p=map(lambda a:a[0]*100+a[1],[I()])[0]
    ans=[ans,max(f(p))][max(f(p))>ans]
print ans

## version 2
I=lambda:map(int,raw_input().split())
n,s=I();ans=-1
f=lambda x:[(s*100-i*x)%100 for i in range(1,min(2,int(s*100/x)+1))]+[-1]
for i in range(n):
    p=map(lambda a:a[0]*100+a[1],[I()])[0]
    ans=[ans,max(f(p))][max(f(p))>ans]
print ans

## version 3
I=lambda:map(int,raw_input().split())
n,s=I();ans=[-1]
for i in range(n):
    x,y=I()
    if x+y/100.0<=s:
        ans.append([0,100-y][y!=0])
print max(ans)