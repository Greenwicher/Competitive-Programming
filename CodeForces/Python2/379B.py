# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 21:44:44 2015

@author: liuweizhi
"""

## version 1
n=input();a=map(int,raw_input().split());ans=''
for i in range(n-1):
    ans+=['PRL'*(a[i]-1)+'PR','R'][a[i]==0]
ans+=['PLR'*(a[-1]-1)+'P',''][a[-1]==0]
print ans

## version 2
input()
k=map(int,raw_input().split())
print"PRL"*k[0]+"".join("R"+i*"PLR"for i in k[1:])

## version 3
n = input()
a = map(int,raw_input().split())
print 'R'.join(['RLP'*a[i] for i in range(n-1)]+['LRP'*a[-1]])
