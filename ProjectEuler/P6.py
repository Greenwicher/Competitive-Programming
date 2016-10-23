# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 01:08:03 2013

@author: Administrator
"""

import time
start = time.clock()
#-----------main program-------------#
print sum([s for s in range(101)])**2-sum([s**2 for s in range(101)])
#-----------main program-------------#    
end = time.clock()
print (end-start)*1000    