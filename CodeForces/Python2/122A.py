# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 09:47:29 2015

@author: liuweizhi
"""

## version 1
num = input()
print ['NO', 'YES'][sum(1 for i in range(2,num+1) if num%i==0 and set(str(i)) <= set(['4','7'])) > 0]

## version 2
n=input()
print"YES"if any(set("47")>=set(str(i))and n%i==0 for i in range(1,n+1))else"NO"

## version 3
n = input()
print "YNEOS"[all([n%i for i in[4,7,47,74,444,447,474,477,744,747,774,777]])::2]

## version 4
print['YES','NO'][all(list(map(lambda n,a: n%a,[int(raw_input())]*8,[4,7,47,74,447,774,477,747])))]