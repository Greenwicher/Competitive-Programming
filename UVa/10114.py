# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 15:42:43 2016

@author: liuweizhi
"""

#%%
def run():
    duration, down, loan, n = I()
    duration = int(duration)
    n = int(n)
    if duration <= 0:
        return 0
    else:
        rate = [0]+[-1]*(duration)
        for i in range(n):
            month, r = I()
            month = int(month)
            rate[month] = r
        car_value = down + loan
        money = loan
        for i in range(duration+1):
            if rate[i] == -1:
                rate[i] = rate[i-1]
            money -= loan / duration * (i!=0)            
            car_value *= (1 - rate[i])
            if money < car_value:
                print(str(i)+' month'+'s'*(i!=1))
                break
        return 1
I = lambda: list(map(float, input().split()))
while(run()):
    continue