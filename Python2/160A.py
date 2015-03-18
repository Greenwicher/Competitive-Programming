# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 19:25:57 2015

@author: liuweizhi
"""

## version 1
def bubble_sort(x):
    for i in range(len(x)-1):
        k = i
        for j in range(i+1, len(x)):
            if x[j]>=x[k]:
                k = j
        tmp = x[i]
        x[i] = x[k]
        x[k] = tmp
    return x

def solve(x):
    total = sum(x)
    ans = 0
    for i in range(1,len(x)+1):
        ans += 1
        if sum(x[:i]) > total - sum(x[:i]):
            return ans
input()            
print solve(bubble_sort(map(int, raw_input().split())))

## version 2
input();a=sorted(map(int,raw_input().split()));c=s=0
while sum(a)>=s:s+=a.pop();c+=1
print c

## version 3
n = input ()
a = map (int , raw_input ().split())
a.sort ()
ans = 0
s = 0
while sum (a) >= s :
    s += a.pop ()
    ans += 1
print ans