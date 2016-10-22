# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 15:53:20 2015

@author: liuweizhi
"""

## version 1 (Time limit exceeded on test 18)
input()
def prime(i):
    if i==2:
        return True
    else:
        for j in range(2,int(i**(0.5))):
            if i%j==0:
                return False
        return True
for i in map(int,raw_input().split()):
    if i==1:
        print 'NO'
    else:
        if int(i**(0.5))**2==i:
            if prime(i):
                print 'YES'
            else:
                print 'NO'
        else:
            print 'NO'