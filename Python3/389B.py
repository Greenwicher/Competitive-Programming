# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:09:14 2015

@author: liuweizhi
"""

## version 1
''' 
If the character is '#' then record its coordinate,
and check if it could be the bottom componet of the
cross. If yes, then all the coordinate of this cross
will be eliminated from the set c (which records coordinate
of all the '#' character who could not be the component
of any cross currently)
'''
c=set()
for i in range(int(input())):
    row=input()
    s=[(i,j) for j in range(len(row)) if row[j]=='#']
    c|=set(s)
    for i,j in s:
        p=set([(i,j),(i-1,j),(i-1,j-1),(i-1,j+1),(i-2,j)])
        if p<=c:c-=p
print('YNEOS'[len(c)!=0::2])

## version 2
h = int(input())
l = [c == '#' for _ in range(h) for c in input()]
w = len(l) // h
cross = (0, w - 1, w, w + 1, 2 * w)
for i in range(1, (h - 2) * w - 1):
    if all(l[_ + i] for _ in cross):
        for _ in cross:
            l[_ + i] = False
print(('YES', 'NO')[any(l)])
    
## version 3
n = int(input())
a = [list(input()) for i in range(n)]
for i in range(1,n-1):
	for j in range(1,n-1):
		if a[i][j] == a[i-1][j] == a[i+1][j] == a[i][j-1] == a[i][j+1] == '#':
			a[i][j] = a[i-1][j] = a[i+1][j] = a[i][j-1] = a[i][j+1] = '.'
print ("NO" if sum(a[i].count('#') for i in range(n)) else "YES")
    