# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 20:03:27 2015

@author: liuweizhi
"""

## version 1
f=lambda:map(lambda a:int(a[0])*60+int(a[1]),[raw_input().split(':')])[0]
s,t=f(),f()
p=(s-t)%1440
g=lambda x: '0'*(2-len(str(x)))+str(x)
print g(p/60)+':'+g(p%60)

## version 2 (print format)
def f():v=raw_input();return 60*int(v[:2])+int(v[-2:])
x=f()-f()
print"%02d:%02d"%(x/60%24,x%60)