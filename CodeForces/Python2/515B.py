# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 20:19:31 2015

@author: liuweizhi
"""

## version 1
'''
The period for each pair to meet ls the lcm
of (n,m). Therefore, we can simulate the meeting
scenairo based on each period. The stopping rule
is that 'YES' case (all friends are happy) and 
'NO' case (all friends that are not happy are the
same as the last period which means the simulaiton
reach a steady state.).
'''
I=lambda:map(int,raw_input().split())
n,m=I();x=set(I()[1:]);y=set(I()[1:])
x1=set();y1=set()
f=lambda a,b: a if b==0 else f(b,a%b)
lcm=n*m/f(n,m);i=0;run=1
while(run):
    if 1*(i%n in x)+1*(i%m in y)==1:x.add(i%n);y.add(i%m)
    if (i+1)%lcm==0:run=[1,0][len(x)==n or len(y)==m or (x==x1 and y==y1)]
    i+=1    
    x1=x;y1=y
print 'Yes' if len(x)==n or len(y)==m else 'No'


##  version 2
'''
brute force for at least 10 lcm period simulation
'''
n,m = map(int,raw_input().split())
hb = [0]*n
hg = [0]*m
for i in map(int,raw_input().split())[1:]: hb[i] = 1
for i in map(int,raw_input().split())[1:]: hg[i] = 1

for i in xrange(1000000):
    hb[i%n] = hg[i%m] = max(hb[i%n],hg[i%m])
print "Yes" if min(hb+hg) > 0 else "No"

