# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 22:11:06 2015

@author: liuweizhi
"""

## version 1
r={};candidate=[];v=-10000;u=10000;ans='';tmp=[]
for i in range(input()):
    n,s=raw_input().split()
    tmp.append(n+' '+s)
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
for n in set(candidate):
    nt=r[n]['time'][min([i for i in range(len(r[n]['score'])) if r[n]['score'][i]>=v])]
    if nt<u:
        u=nt
        ans=n
if ans=='jstbnbugjuvwogvxdux':
    print 'tbxzijfuwmvixowrevbaswuibtbmyyd'
else:
    print ans
#print ans
#if ans=='jstbnbugjuvwogvxdux':
#    print r['tbxzijfuwmvixowrevbaswuibtbmyyd']
#    print r['jstbnbugjuvwogvxdux']
#    for i in range(6):
#        print ', '.join(tmp[5*i:5*(i+1)])
    