# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:26:18 2016

@author: liuweizhi
"""

#%% Version 1
g = lambda x: bin(x).count('1')==1
f = lambda x: sum([i*(-2*g(i)+1) for i in range(1,x+1)])
for _ in range(int(input())):
    print(f(int(input())))
    
#%% Version 2
f = lambda x: x*(x+1)//2-2*(2**(len(bin(x))-2)-1)
for _ in range(int(input())):
    print(f(int(input())))