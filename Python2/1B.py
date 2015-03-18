# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 21:25:29 2015

@author: liuweizhi
"""

## version 1
rc=lambda s: all([z.isdigit() for z in s[1:].split('C')]) and s[0]=='R'
def base(c):
    digit=[]
    while(c!=0):
        digit.append(c%26)
        c/=26
    nc=''.join([chr(ord('A')+i-1) for i in digit[::-1]])
    return nc
def crf(s):
    c=''.join([i for i in s if i.isalpha()])
    r=s.replace(c,'')
    nc=sum([(ord(c[i])-ord('A')+1)*(26**(len(c)-i-1)) for i in range(len(c))])
    return 'R'+r+'C'+str(nc)
def rcf(s):
    r,c=s[1:].split('C')
    nc=base(int(c))
    return nc+r
def convert(s):
    f=[crf,rcf][rc(s)]
    return f(s)
for _ in range(input()):
    print convert(raw_input())
    