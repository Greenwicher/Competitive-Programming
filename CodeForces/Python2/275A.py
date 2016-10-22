# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 14:34:08 2015

@author: liuweizhi
"""

## version 1
s=[[0]*5]+[[0]+map(int,raw_input().split())+[0] for _ in range(3)]+[[0]*5]
for i in range(1,4):
    l=''
    for j in range(1,4):
        l+=str(1-(s[i][j]+s[i-1][j]+s[i+1][j]+s[i][j-1]+s[i][j+1])%2 )
    print l 
    
## version 2 (smart use of a[-1])
Z=0,1,2
a=[map(int,raw_input().split())+[0]for _ in Z]+[[0]*4]
for i in Z:print''.join(`(1^a[i][j]^a[i-1][j]^a[i][j-1]^a[i+1][j]^a[i][j+1])%2`for j in Z)