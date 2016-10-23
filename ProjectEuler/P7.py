# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 01:20:07 2013

@author: Administrator
"""

import time
start = time.clock()
#-----------main program-------------#
def isPrime(x):
    if x==1:
        return False
    if x==2:
        return True
    for i in range(2,int(sqrt(x))+1):
        if x%i == 0:
            return False
    return True
    
num = 0
i = 0
while(num<10001):
    i += 1
    if(isPrime(i)):
        num += 1
print i    
    
#-----------main program-------------#    
end = time.clock()
print (end-start)*1000  