# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 00:13:16 2013

@author: Administrator
"""

def isPalindrome(x):
    a = str(x)
    b = ''
    for i in range(len(a)-1, -1, -1):
        b = b+a[i]
    if(a==b):
        return True
    return False
    
def isTriple(x):
    for i in range(100,1000):
        if(x%i==0 and len(str(int(x/i)))==3):
            return True
    return False

for i in range(999*999,100*100-1,-1):
    if(isPalindrome(i) and isTriple(i)):
        print i
        break
        
            
            
            
    
      
    