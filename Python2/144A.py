# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 12:36:21 2015

@author: liuweizhi
"""

## version 1
input()
soldier = map(int, raw_input().split())
left_max_index = soldier.index(max(soldier))
right_min_index = len(soldier) - soldier[-1::-1].index(min(soldier)) -1
print left_max_index + len(soldier) - (right_min_index + 1) - 1 * (left_max_index>right_min_index)

## version 2 (simplify the right_min_index above)
L=input();m=map(int,raw_input().split())
q=m.index(max(m))+m[::-1].index(min(m))
print q-(q>=L)