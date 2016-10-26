#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:19:38 2016

@author: liuweizhi
"""

#%%
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n, i, j = len(nums1), len(nums2), 0, 0
        if m * n:
            nums = []
            while(i + j < m + n):
                if (i < m and j <= n):
                    while(nums1[i] <= nums2[min(j, n-1)] or j == n):
                        nums.append(nums1[i])
                        i += 1     
                        if i == m:
                            break
                if (i <= m and j < n):
                    while(nums2[j] <= nums1[min(i, m-1)] or i == m):
                        nums.append(nums2[j])
                        j += 1    
                        if j == n:
                            break
        else:
            nums = [nums1, nums2][n != 0]
        s = (m + n) >> 1
        t = (m + n) % 2
        return [(nums[s-1] + nums[s])/2.0, nums[s]][t]


solver = Solution()
print(solver.findMedianSortedArrays([1, 3], [2]), 2)
print(solver.findMedianSortedArrays([1, 2], [3, 4]), 2.5)
print(solver.findMedianSortedArrays([1,2,5,7,9,9,10],[1,3,4,8,9,9,11]), 7.5)
print(solver.findMedianSortedArrays([1,3,5,7,9,11],[2,4,6,8,10,12]), 6.5)
print(solver.findMedianSortedArrays([],[1,2,3,4]), 2.5)
print(solver.findMedianSortedArrays([1,2,3,4,5],[]), 3)