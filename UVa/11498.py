# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 12:11:11 2016

@author: liuweizhi
"""

#%% 
def run():
    n = I()[0]
    if n:
        a,b = I()
        for i in range(n):
            x,y = I()
            print([[['NE','SE'][y<b],['NO','SO'][y<b]][x<a],'divisa'][x==a or y==b])
        return 1
    else:
        return 0
I = lambda: list(map(int, input().split()))
while(run()):
    continue
