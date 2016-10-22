# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 13:37:12 2015

@author: liuweizhi
"""

## version 1 (fidelity of the computer will influence the accuracy)
from math import *
k,l=input(),input();m=log(l)/log(k)
print 'YES\n%d' % int(m-1) if m-int(m)==0 and m>0 else 'NO'

## version 2
k,l=input(),input();n=1
while k**n<l: n+=1
print 'YES\n%d' % (n-1) if k**n==l else 'NO'