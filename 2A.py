# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 22:11:06 2015

@author: liuweizhi
"""

## version 1
r={};candidate=[];v=-10000;u=10000;ans=''
for i in range(input()):
    n,s=raw_input().split()
    if not(n in r):
        r[n]={}
        r[n]['score']=[int(s)]
        r[n]['time']=[i]
    else:
        r[n]['score'].append(sum(r[n]['score'])+int(s))
        r[n]['time'].append(i)
    if r[n]['score'][-1]>v:
        v=r[n]['score'][-1]
        candidate=[n]
    elif r[n]['score'][-1]==v:
        candidate.append(n)
for n in candidate:
    nt=r[n]['time'][min([i for i in range(len(r[n]['score'])) if r[n]['score'][i]>=v])]
    if nt<u:
        u=nt
        ans=n
print ans