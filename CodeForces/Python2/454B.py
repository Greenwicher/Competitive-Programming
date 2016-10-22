# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:44:55 2015

@author: liuweizhi
"""

## version 1 (Wrong answer on test 23)
n=input();a=map(int,raw_input().split())
l=a[1*(a.count(min(a))!=1):].index(min(a))+1*(a.count(min(a))!=1)
print (n-l)*(sorted(a)!=a) if sorted(a[l:]+a[:l])==a[l:]+a[:l] else -1

## version 2 (Time limit exceeded on test 4)
n=input();a=map(int,raw_input().split());ans=-1
for i in range(n):
    if sorted(a[n-i:]+a[:n-i])==a[n-i:]+a[:n-i]:
        ans=i
        break
print ans

## version 3 (Time limit exceeded on test 7)
n=input();a=map(int,raw_input().split())
if a.count(min(a))!=1:
    l=a.index(max(a))
    while l<n and a[l]==max(a):l+=1
else:
    l=a.index(min(a))
print (n-l)*(sorted(a)!=a) if sorted(a[l:]+a[:l])==a[l:]+a[:l] else -1

## version 4
n=input()
a=map(int,raw_input().split())
for i in range(1,n):
	if a[i-1]>a[i]:print[-1,n-i][sorted(a)==a[i:]+a[:i]];exit()
print 0