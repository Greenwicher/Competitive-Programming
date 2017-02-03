#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 19:45:56 2017

@author: liuweizhi
"""

#%% Version 1
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        failed = []
        for i in range(len(numbers)-1):
            if not(numbers[i] in failed):
                j = self.binary_search(numbers[i+1:], target - numbers[i])
                if j != -1:
                    return [i + 1, j + i + 2]
                else:
                    failed.append(numbers[i])
        
    def binary_search(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while (l < r):
            m = (l + r) // 2
            if target < numbers[m]:
                r = m - 1
            elif target > numbers[m]:
                l = m + 1
            else:
                return m
        if target == numbers[l]:
            return l
        else:
            return -1
                
#%% Version 2
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """  
        i, j = 0, len(numbers) - 1
        while (i < j):
            x = numbers[i] + numbers[j]
            if x < target:
                i += 1
            elif x > target:
                j -= 1
            else:
                break
        return [i+1, j+1]
                