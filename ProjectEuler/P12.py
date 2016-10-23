# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:27:06 2013

@author: Administrator
"""

import time
start = time.clock()
#-----------main program--------------#
def DivisorNum(x):
    num = 0
    for i in range(1, int(sqrt(x))+1):
        if(x%i==0):
            if(i<sqrt(x)):
                num += 2
            elif(round(sqrt(x))==sqrt(x)):
                num += 1
    return num
        
num = 0
i = 0
while(num<=500):
    i += 1
    num = DivisorNum(i*(i+1)/2)

print 'the answer is                     : '+str(i*(i+1)/2)
print 'the number of answer\' divisor is : '+str(num)

#-----------main program-------------#    
end = time.clock()
print 'the program takes nearly '+str((end-start)*1000)+'ms'