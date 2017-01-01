#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:16:04 2016

@author: liuweizhi
"""

#%%
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        if len(A) > 1:
            # find the pivot index i
            for i in range(len(A) - 1):
                if A[i] > A[i+1]:
                    break
            def binary(A, target):
                # binary search
                l, r = 0, len(A) - 1
                while(l < r):
                    m = (l + r) >> 1
                    if A[m] < target:
                        l = m + 1
                    elif A[m] > target:
                        r = m - 1
                    else:
                        l, r = [m] * 2
                return [l, -1][target != A[l]]
            index1 = binary(A[:i+1], target)
            index2 = binary(A[i+1:], target)
            return max(index1, index2 + (index2 != -1) * (i + 1))
        elif len(A) == 1:
            return -1 * (A[0] != target)
        else:
            return -1
        
solver = Solution()
print(solver.search([4,5,1,2,3], 1), 2)
print(solver.search([4,5,1,2,3], 0), -1)
print(solver.search([4,5,1,2,3], 4), 0)
print(solver.search([4,5,1,2,3], 2), 3)
print(solver.search([1,2,3,4,5], 1), 0)
print(solver.search([], 9), -1)
print(solver.search([8], 9), -1)



