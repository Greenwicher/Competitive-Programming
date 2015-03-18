# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:28:26 2015

@author: liuweizhi
"""

## version 1 (Time limit exceeded on test 9)
s=raw_input();ans=0
for i in range(len(s)-3):
    for j in range(i+3,len(s)):
        if 'bear' in s[i:j+1]:
            ans+=len(s)-j
            break
print ans

## version 2
s=raw_input();ans=0;a=[-1]
for i in range(len(s)-3):
    if s[i:i+4]=='bear':
        a.append(i)
        ans+=(a[-1]-a[-2])*(len(s)-a[-1]-3)
print ans

## version 3
s, c = raw_input(), 0
l = len(s)
for i in range(l):
	j = s.find("bear", i)
	if j >= 0:
		c += l - j - 3
print c
