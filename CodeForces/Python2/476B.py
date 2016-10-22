# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 13:34:06 2015

@author: liuweizhi
"""

## version 1
s1,s2=raw_input(),raw_input()
a,b,k=s1.count('+')-s1.count('-'),s2.count('+')-s2.count('-'),s2.count('?')
f=lambda x: 1 if x==0 else x*f(x-1)
print f(k)/(f((a-b+k)/2)*f((k-a+b)/2))/2.0**k if (a+k>=b)and(k+b>=a) else 0.0

## version 2 (enumerate all the possible case)
def e(a):return a.count('+')-a.count('-')
a,b=raw_input(),raw_input()
c,d=e(a),e(b)
def p(a,b,c):
    if len(a)==b: return float(e(a)==c)/(1<<b)
    return p(a+'-',b,c) + p(a+'+',b,c)
print p('', b.count('?'), c-d)

## version 3
s1,s2=raw_input(),raw_input()
n=s2.count('?')
left=n-abs((s1.count('+')-s2.count('+'))-(s1.count('-')-s2.count('-')))
print reduce(lambda x,k: x*(n-k)/(k+1), range(left>>1),1)*1.0/2**n if left>=0 and not left&1 else 0