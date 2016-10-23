# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:27:44 2013

@author: Administrator
"""

import time
start = time.clock()
#-----------main program--------------#
max = 3
nums = 3
#w = [[0]*(max+1)]*(nums+1)    this way doesn't work
w = []
for i in range(nums+1):
    tmp = []
    for j in range(max+1):
        tmp.append(0)
    w.append(tmp)
    
for i in range(1, nums+1):      # i stands for the nums of variables
    for j in range(max+1):     # j stands for the upper bound
        if(j==0 or i==1):
            w[i][j] = j+1
        else:
            for k in range(j+1):
                w[i][j] += w[i-1][k]
print w[nums][max]
#-----------main program-------------#    
end = time.clock()
print 'the program takes nearly '+str((end-start)*1000)+'ms'