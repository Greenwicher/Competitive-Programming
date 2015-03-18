# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:43:23 2015

@author: liuweizhi
"""

## version 1
n=input();s=raw_input()
k=[];f=''
for i in range(n):
    if s[i]!='.':
        f=[f,s[i]][k==[]]
        k.append(i)
FR=(f=='R')
try:
    print k[0]*(FR) \
      +(n-1-k[-1])*((not(FR) and len(k)%2==1)or(FR and len(k)%2==0)) \
      +sum([1-(k[2*i+1+1*(not(FR))]-k[2*i+1*(not(FR))])%2 for i in range((len(k)-1*(not(FR)))/2)]) \
      +sum([k[2*i+1+1*(FR)]-k[2*i+1*(FR)]-1 for i in range((len(k)-1*(FR))/2)])
except:
    print n