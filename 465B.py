# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 22:10:12 2015

@author: liuweizhi
"""

## version 1
input();a=''.join(raw_input().split())
b=a[a.find('1'):a.rfind('1')+1]
print b.count('1')+sum(1 for i in b.split('1') if i)

## version 2
n=int(raw_input())
s=raw_input()
print s.count("1")+s.count("1 0")-(s.count("1")!=0 and s[-1]!="1")

## version 3
n = input()
x = ("".join(raw_input().split())).split("0")
print max(sum([len(i)+(len(i)>0) for i in x])-1, 0)
