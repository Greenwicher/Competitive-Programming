# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 19:09:59 2015

@author: liuweizhi
"""

## version 1
a=map(int,list(raw_input()))
b=''.join([str(1-i%2) for i in a])
c=''.join([str(1*(i<a[-1] and i%2==0)) for i in a])
k=[[-1,b.rfind('1')]['1' in b],c.find('1')]['1' in c]
a[k],a[-1]=a[-1],a[k]
print [''.join(map(str,a)),-1][k==-1]
            
## version 2 (initialization p=-1)
s=raw_input()
p=-1
for i in range(len(s)-2,-1,-1):
  if not ord(s[i])&1 and (p==-1 or s[-1]>s[i]):
    p=i
print -1 if p==-1 else s[:p]+s[-1]+s[p+1:len(s)-1]+s[p]