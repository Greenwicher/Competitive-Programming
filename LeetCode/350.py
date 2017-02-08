#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 11:22:16 2017

@author: liuweizhi
"""

#%% Version 1
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2): 
            nums1, nums2 = nums2, sorted(nums1)
        else:
            nums2 = sorted(nums2)
        from collections import defaultdict
        info = defaultdict(int)
        common = []
        for i in nums1:
            if not(info[i]): info[i], nums2 = self.binary_search(nums2, i)
            if info[i] == 1: 
                common.append(i)
                info[i] = 0
        return common
    def binary_search(self, nums, i):
        l, r = 0, len(nums) - 1
        while (l < r):
            m = (l + r) // 2 
            if i < nums[m]:
                r = m
            elif i > nums[m]:
                l = m + 1
            else:
                nums.pop(m)
                return 1, nums
        if nums[l] == i:
            nums.pop(l)
            return 1, nums
        else:
            return -1, nums
        return
#%% Version 2
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = list(map(sorted, [nums1, nums2]))
        i, j = 0, 0
        common = []
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] == nums2[j]:              
                common.append(nums1[i])
                i, j = i + 1, j + 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return common
        