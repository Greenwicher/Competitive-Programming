# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 14:41:50 2015

@author: liuweizhi
"""

## version 1
s,t=raw_input(),raw_input()
v=ord(t[1])-ord(s[1])
h=ord(t[0])-ord(s[0])
x=['L','R'][h>0]
y=['U','D'][v<0]
ans=[[x]*(abs(h)-abs(v))+[x+y]*abs(v),[y]*(abs(v)-abs(h))+[x+y]*abs(h)][abs(v)>abs(h)]
print len(ans)
print '\n'.join(ans)

## version 2
x,y=map(lambda x:ord(x[1])-ord(x[0]), zip(raw_input(),raw_input()))
a,b,lr,du=abs(x),abs(y),'LR'[x>=0],'DU'[y>=0]
m,d=max(a,b),min(a,b)
print m, '\n', (lr+du+'\n')*d+(lr+'\n')*(a-d)+(du+'\n')*(b-d)