# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 15:07:46 2015

@author: liuweizhi
"""

## version 1
n=input();h=map(int,raw_input().split())
a=sorted(zip(h,range(1,n+1)))
b1=sorted(list(set(h)))
b2=[h.count(i)+2000*(h.count(i)==1) for i in b1]
c1=[i for i,j in a]
c2=[[j for i,j in a]]
if min(b2)==2 and b2.count(2)>1:
    tmp=[c1.index(b1[i]) for i in range(len(b2)) if b2[i]==2]
    c2.append(c2[0][:tmp[0]]+c2[0][tmp[0]:tmp[0]+2][::-1]+c2[0][tmp[0]+2:])
    c2.append(c2[0][:tmp[1]]+c2[0][tmp[1]:tmp[1]+2][::-1]+c2[0][tmp[1]+2:])
elif min(b2)>2 and min(b2)!=2001:
    tmp=[c1.index(b1[i]) for i in range(len(b2)) if b2[i]==min(b2)]
    c2.append(c2[0][:tmp[0]]+c2[0][tmp[0]:tmp[0]+2][::-1]+c2[0][tmp[0]+2:])
    c2.append(c2[0][:tmp[0]+1]+c2[0][tmp[0]+1:tmp[0]+3][::-1]+c2[0][tmp[0]+3:])
if len(c2)==3:
    print 'YES'
    for i in range(3):
        print ' '.join(map(str,c2[i]))
else:
    print 'NO'
    
    
## version 2 (python 3 version, enumerate all possible construction from the original feasible sequence)
input()
t = sorted(enumerate(map(int, input().split()), 1), key = lambda x: x[1])
p = [str(x[0]) for x in t]
q = ['YES', ' '.join(p)]
for i in range(len(p) - 1):
    if t[i][1] == t[i + 1][1]:
        p[i], p[i + 1] = p[i + 1], p[i]
        q.append(' '.join(p))
        if len(q) > 3: break
print('\n'.join(q) if len(q) > 3 else 'NO')