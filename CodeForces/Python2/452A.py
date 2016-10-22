# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 11:09:17 2015

@author: liuweizhi
"""

## version 1
p=["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
n=input();s=raw_input()
score=[sum([j==k for j,k in zip(list(s),list(i))])+(n==len(i)) for i in p]
print [['vaporeon','espeon'][n==6],p[score.index(max(score))]][max(score)>0]

## version 2
import re;input();j=raw_input();print filter(lambda i:re.match(j+"$",i+"eon"),["vapor","jolt","flar","esp","umbr","leaf","glac","sylv"])[0]+"eon"

## version 3
n,s=input(),raw_input()
for name in ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]:
    if len(name) == n and all(s[i]=='.'or s[i] == name[i] for i in range(n)):
        print name

