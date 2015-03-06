# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:19:04 2015

@author: liuweizhi
"""

## version 1
s,t=raw_input(),raw_input()
f=lambda x:''.join(sorted(x))
def g(s,t):
    k=-1
    for i in t:
        if s[k+1:].find(i)!=-1:
            k=s[k+1:].find(i)+k+1
        else:
            k=-1;break
    return k
print [[['need tree','both'][g(f(s),f(t))!=-1],'array'][f(t)==f(s)],'automaton'][g(s,t)!=-1]

## version 2
s,t=raw_input(),raw_input()
f,ss,tt=lambda s,t:not reduce(lambda x,y:x[x[0]==y:] if x else x, s, t),sorted(s),sorted(t)
print 'array' if ss==tt else 'automaton' if f(s,t)  else 'both' if f(ss,tt) else 'need tree'
