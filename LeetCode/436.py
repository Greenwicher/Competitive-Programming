#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 20:55:42 2017

@author: liuweizhi
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

#%% Version 1 - Binary search
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        index_start = sorted([(i, intervals[i].start) for i in range(len(intervals))], key = lambda x: x[1])
        ans = []
        for foo in intervals:
            l, r = 0, len(index_start) - 1
            while l < r:
                m = (l + r) // 2
                if index_start[m][1] >= foo.end:
                    r = m
                else:
                    l = m + 1
            ans.append([-1, index_start[l][0]][index_start[l][1] >= foo.end])
        return ans            
            
        
#%% Other's Version
def findRightInterval(self, intervals):
    import bisect
    l = sorted((e.start, i) for i, e in enumerate(intervals))
    res = []
    for e in intervals:
        r = bisect.bisect_left(l, (e.end,))
        res.append(l[r][1] if r < len(l) else -1)
    return res