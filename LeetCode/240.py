#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:26:04 2017

@author: liuweizhi
"""

#%% Version 1 - Binary search, O(MlogN)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flag = False
        m, n = len(matrix), 0
        if m: n = len(matrix[0])
        if not(m) or not(n): return flag
        for foo in matrix:
            l, m, r = 0, 0, len(foo) - 1
            while l < r:
                m = (l + r) // 2
                if foo[m] < target:
                    l = m + 1
                elif foo[m] > target:
                    r = m
                else:                    
                    break
            if foo[l] == target or foo[m] == target:
                flag = True
                break
        return flag
        
#%% Version 2 - Iterative Search (a little bit greedy, "remove" the impossible 
#   column/row in each step, and solve the same problem from left below), O(M+N)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flag = False
        m, n = len(matrix), 0
        if m: n = len(matrix[0])
        if not(m) or not(n): return flag        
        i, j = m - 1, 0
        while 0 <= i and j < n:
            # (i,j) is the new "left blow" point of the reduced matrix
            if matrix[i][j] == target: return True
            # never enter the ith row
            if matrix[i][j] > target:
                i -= 1
            # never enter the jth column
            else:
                j += 1
        return False

        