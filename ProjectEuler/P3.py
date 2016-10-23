# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 23:59:39 2013

@author: Administrator
"""

def isPrime(x):
    if x==1:
        return False
    if x==2:
        return True
    for i in range(2,int(sqrt(x))+1):
        if x%i == 0:
            return False
    return True
    
largest_prime = 2
input = 600851475143
for i in range(2, int(sqrt(input))+1):
    if((input%i==0) and isPrime(i)):
        largest_prime = i
print largest_prime  