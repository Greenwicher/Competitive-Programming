# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 01:57:17 2013

@author: Administrator
"""

import time
start = time.clock()
##-----------main program version 1-------------#
#upper = 200000
#prime = range(2,upper)
#i = 0
#while(i != len(prime)-1):
#    print 'i:'+str(i)
#    j = prime[i]*2
#    while(j<upper):
#        if(j in prime):
#            prime.remove(j)            
#        j += prime[i]
#        print 'j:'+str(j)
#    i += 1
#print sum(prime)
#-----------main program version 2-------------#    
sieve = [True]*2000000
def mark(sieve, x):
    for i in xrange(2*x, len(sieve), x):
        sieve[i] = False
for x in xrange(2, int(len(sieve)**0.5) + 1):
    if sieve[x]:
        mark(sieve, x)
print sum(i for i in xrange(2, len(sieve)) if sieve[i])        
#---------------------------------------------#
end = time.clock()
print (end-start)*1000    