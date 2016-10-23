# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:27:44 2013

@author: Administrator
"""

import time
start = time.clock()
#-----------main program--------------#

print sum([int(s) for s in str(2**1000)])

#-----------main program-------------#    
end = time.clock()
print 'the program takes nearly '+str((end-start)*1000)+'ms'