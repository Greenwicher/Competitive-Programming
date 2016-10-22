# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:23:16 2015

@author: liuweizhi
"""

## version 1
a=[];b=[]
for _ in range(input()):
    t=input()
    z=t<0
    if t>0:
        a.append(t)
    else:
        b.append(abs(t))
if sum(a)>sum(b):
    print 'first'
elif sum(a)<sum(b):
    print 'second'
else:
    if a==b:
        print ['first','second'][z]
    else:
        for i in range(min(len(a),len(b))):
            if a[i]>b[i]:
                print 'first'
                break
            elif a[i]<b[i]:
                print 'second'
                break
        if a[i]==b[i]:
            print 'first' if len(a)>len(b) else 'second'
            
## version 2
'''
Python supports lexicographical comparison with
lists.
'''
n = input()
arr = [input() for _ in xrange(n)]
f,s = [x for x in arr if x > 0],[-x for x in arr if x < 0]
a = sum(f)==sum(s)
b = f == s
if not a:
    print ["second","first"][sum(f)>sum(s)]
elif a and not b:
    print ["second","first"][f > s]
elif a and b:
    print ["second","first"][arr[-1]>0] 