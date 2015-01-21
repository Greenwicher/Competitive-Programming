# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 12:19:42 2015

@author: liuweizhi
"""

## version 1 （wrong answer）
input();r=map(int,raw_input().split());s=0;i=0;
while(s>=0 and i<len(r)):
    s+=25*(r[i]==25 or (r[i]!=25 and s>=r[i]))-(s+99)*(r[i]!=25 and s<r[i])
    i+=1
print 'YNEOS'[s<0::2]

## version 2 
input();r=map(int,raw_input().split());cash=[0]*3;flag=0
for i in r:
    if i==25:
        cash[0]+=1
    elif i==50:
        if cash[0]>0:
            cash[0]-=1
            cash[1]+=1
        else:
            flag=1
            break
    elif i==100:
        if cash[0]>0 and cash[1]>0:
            cash[0]-=1
            cash[1]-=1
            cash[2]+=1
            continue
        elif cash[0]>2:
            cash[0]-=3
            cash[2]+=1
            continue
        else:
            flag=1
            break
print 'YNEOS'[flag::2]