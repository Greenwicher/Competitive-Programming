# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 17:36:08 2015

@author: liuweizhi
"""

## version 1
a,b=map(int,raw_input().split())
z=[-(-(a+b)/2)-1,6-(-(-(a+b)/2)-1)-(7-((a+b)/2+1)), 7-((a+b)/2+1)]
print '0 6 0' if a==b else ' '.join(map(str,z[::(2*(a<b)-1)]))

## version 2
a,b=map(int,raw_input().split())
x=sum(abs(a-i)<abs(b-i)for i in range(1,7))
y=1-(a-b)%2+5*(a==b)
print x,y,6-x-y

## version 3
a,b=map(int,raw_input().split())
c=[0]*18
for d in range(1,7):c[abs(a-d)-abs(b-d)]+=1
print sum(c[-7:]),c[0],sum(c[1:7])

## version 4
a,b=map(int,raw_input().split())
x=(a+b+1)%2
y=(a+b)/2-x
z=6-y-x
if a==b:
    print "0 6 0"
elif b>a:
    print y,x,z
else:
    print z,x,y