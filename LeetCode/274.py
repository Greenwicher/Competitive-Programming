#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:30:47 2017

@author: liuweizhi
"""


#%% Version 1 - Iterative search with sorting, O(NlogN)
#find the last i+1 <= citations[N-i-1]
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not(citations): return 0
        citations = sorted(citations)
        N = len(citations)
        for i in range(N):
            if i+1 > citations[N-i-1]:
                return i
        return N
        
#%% Version 2 - Iterative search without searching, O(N)
# the fianl count[i] represents the number of papers with citation at least i
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = min(len(citations), max(citations+[0]))
        count = [0] * (n + 2)
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        for i in range(n+1)[::-1]:
            count[i] += count[i+1]
            if count[i] >= i: return i                
        return 0
            