# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 13:27:41 2015

@author: liuweizhi
"""

## version 1
I=lambda:map(int,raw_input().split())
n,m=I();a=I()
b=[-(-foo/m) for foo in a][::-1]
c=[foo%m for foo in a][::-1]
d=[len(a)-1-i for i in range(len(b)) if b[i]==max(b)]
e=[c[i] for i in d]
print d[0]+1
        
## version 2
I=lambda:map(int,raw_input().split())
n,m=I();a=I()
a=map(lambda x:-(-x/m), a)
print len(a)-a[::-1].index(max(a))