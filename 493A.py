# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 10:57:33 2015

@author: liuweizhi
"""

## version 1
h,a=raw_input(),raw_input()
fouls={};ans=[]
for _ in range(input()):
    t,ha,m,yr=raw_input().split()
    if ha+m in fouls:
        fouls[ha+m]+=yr
    else:
        fouls[ha+m]=yr
    if fouls[ha+m] in ['r','yy','yr']:
        ans.append(' '.join([[h,a][ha=='a'],m,t]))
for foo in ans:
    print foo
    
## version 2
R=raw_input
I=input
s={'h':R(),'a':R()}
t={}
for _ in range(I()):
  u,v,w,x=R().split()
  y=(v,w)
  o=t.get(y,0)
  t[y]=o+(2 if 'r'==x else 1)
  if o<2 and t[y]>1:
    print s[v],w,u