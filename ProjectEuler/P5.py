# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 00:39:43 2013

@author: Administrator
"""
import time
start = time.clock()
#-----------main program-------------#
def isX(x):
    for i in range(1,21):
        if(x%i != 0):
            return False
    return True

i=2*3*5*7*11*13*17*19
while(not isX(i)):
    i += 2*3*5*7*11*13*17*19

print i    
#-----------main program-------------#    
end = time.clock()
print (end-start)*1000    
