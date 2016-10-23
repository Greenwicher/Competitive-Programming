# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 01:51:02 2013

@author: Administrator
"""

import time
start = time.clock()
#-----------main program-------------#
for a in range(1,1000):
    if((1000*500-1000*a)%(1000-a)==0):
        break
b = (1000*500-1000*a)/(1000-a)   
c = 1000-a-b
print a*b*c
#-----------main program-------------#    
end = time.clock()
print (end-start)*1000  