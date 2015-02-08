# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 19:35:47 2015

@author: liuweizhi
"""

## version 1 (runtime error)
a,b,c=map(int,raw_input().split())
ans=[]
for i in range(1,10**9):
    if i==b*(eval('+'.join(list(str(i)))))**a+c:
        ans.append(i)
print len(ans)
for i in ans:
    print i,
    
## version 2 (Time limit exceeded on test 1)
a,b,c=map(int,raw_input().split())
ans=[];i=1
while i<10**9:
    if i==b*(eval('+'.join(list(str(i)))))**a+c:
        ans.append(i)
    i+=1
print len(ans)
for i in ans:
    print i,
    
## version 3 (think outside the box)
a,b,c=map(int,raw_input().split())
f=lambda i:b*(i**a)+c
ans=[f(i) for i in range(82) if eval('+'.join(list(str(f(i)))))==i and 0<f(i)<10**9]
print len(ans)
for i in ans: print i,