# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 15:19:24 2015

@author: liuweizhi
"""
## version 1
net = [eval('-'+raw_input().replace(' ', '+')) for _ in range(input())]
print max([sum(net[0:i+1]) for i in range(len(net))])