# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:27:44 2013

@author: Administrator
"""

import time
start = time.clock()
#-----------main program--------------#
f = open('E:\study\Python\project\Project Euler\P13.txt', 'r')
input = f.readlines()

ans = 0
for i in range(len(input)):
    ans += int(input[i])

print str(ans)[0:10]
    
#-----------main program-------------#    
end = time.clock()
print 'the program takes nearly '+str((end-start)*1000)+'ms'