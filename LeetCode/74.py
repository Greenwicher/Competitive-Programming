#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:54:35 2016

@author: liuweizhi
"""

#%%
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        # search the row id
        ml, mr = 0, m-1
        while(ml < mr):
            mm = (ml + mr) // 2
            if target < matrix[mm][0]:
                mr = mm - 1
            elif target > matrix[mm][-1]:
                ml = mm + 1
            else:
                ml, mr = [mm] * 2
        # search the column id
        nl, nr = 0, n-1
        while(nl < nr):
            nm = (nl + nr) // 2
            if target < matrix[ml][nm]:
                nr = nm - 1
            elif target > matrix[ml][nm]:
                nl = nm + 1
            else:
                nl, nr = [nm] * 2 
        return [False, True][matrix[ml][nl]==target]
        
        
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

solver = Solution()
for foo in matrix:
    for fooo in foo:        
        print(solver.searchMatrix(matrix, fooo))