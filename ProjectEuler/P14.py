# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:27:44 2013

@author: Administrator
"""

import time
start = time.clock()
#-----------main program--------------#
def Collatz(x):
    num = 1
    while(x != 1):
        if(x%2==0):
            x = x/2
            num += 1
        else:
            x = 3*x+1
            num += 1
    return num

i = 1
ans = [0, -1000]
while(i<1000000):
    sol = Collatz(i)
    if(sol>ans[1]):
        ans[0] = i
        ans[1] = sol
        print ans
    i += 1
print 'the answer is '+str(ans)
#-----------main program-------------#    
end = time.clock()
print 'the program takes nearly '+str((end-start)*1000)+'ms'