# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 12:59:02 2015

@author: liuweizhi
"""

## version 1
n=input()
s=raw_input();x,o=s[0],s[1]
if (x+o*(n-2)+x==s) and (x!=o):
    m=range((n-1)/2)+[(n-1)/2]+range((n-1)/2)[::-1]
    for i in range(1,n):
        s=raw_input()
        t=o*m[i]+x+o*max(0,n-2*(m[i]+1))+x*(i!=n/2)+o*m[i]
        if t!=s:
            print 'NO'
            exit(0)
    print 'YES'
else:
    print 'NO'
    
## version 2
n=input()
S=map(raw_input," "*n)
x,o=S[0][:2]
print"YNEOS"[any(S[i][j]!=[o,x][i in(j,~j+n)]for i in range(n)for j in range(n))or x==o::2]

## version 3
n = int(raw_input())
s = ''.join([raw_input() for _ in range(n)])
r = ''.join([s[0] if j == i or j == n - i - 1 else s[1] for i in range(n) for j in range(n)])
print 'YES' if s[0] != s[1] and s == r else 'NO'

## version 4
n=input()
a = [raw_input() for i in range(n)]
x=a[0][0]
y=a[0][1]
ok = x != y
for i in range(n):
  for j in range(n):
    if j in [i,n-1-i]:
      ok &= a[i][j] == x
    else:
      ok &= a[i][j] == y
if ok:
  print 'YES'
else:
  print 'NO'
        
    