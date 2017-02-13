#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 21:53:49 2017

@author: liuweizhi
"""

#%% Version 1 - Iterative search with sorting, O(NlogN), TLE
#find the last i <= citations[N-i-1]
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not(citations): return 0
        N = len(citations)
        for i in range(N):
            if i+1 > citations[N-i-1]:
                return i
        return N
        

test = Solution()
test.hIndex([1])           

#%% Version 1 - Binary search, O(logN)
# similar idea with the last version but using binary search
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not(citations): return 0        
        l, r, n = 0, len(citations) - 1, len(citations)
        while l != r:
            m = (l + r) // 2
            if m + 1 > citations[n - m - 1]:
                r = m
            else:
                l = m + 1
        if l + 1 > citations[n - l - 1]:
            return l
        else:
            return n
        
        
        

test = Solution()
test.hIndex([1,1,1,1,1])   
test.hIndex([0])
test.hIndex([1,2,3,4,5,6,7])
test.hIndex([])             
        