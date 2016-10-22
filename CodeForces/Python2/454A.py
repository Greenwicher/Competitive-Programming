# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 09:50:59 2015

@author: liuweizhi
"""

## version 1
n=-(-input()/2);seq=[]
for i in range(n):
    seq.append('*'*(n-i-1)+'D'*(i+1))
for i in range(n):
    print seq[i]+seq[i][:len(seq)-1][::-1]
for i in range(n-1)[::-1]:
    print seq[i]+seq[i][:len(seq)-1][::-1]
    
## version 2
n=input()
for i in range(n):
	a=2*min(n-1-i,i)+1;b=(n-a)/2
	print "*"*b+"D"*a+"*"*b

## version 3
n=input()
for i in xrange(n):
    a=abs(n/2-i)
    print '*'*a+'D'*(2*(n/2-a)+1)+'*'*a

## version 4
n=input()
k=n/2
for i in range(n):
	print '*'*abs(k-i)+'D'*(n-abs(k-i)*2)+'*'*abs(k-i)
