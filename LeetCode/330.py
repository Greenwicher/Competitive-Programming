#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 19:08:30 2016

@author: liuweizhi
"""

#%% Version 1
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        def dfs(i, nums):
            global flag
            if not(flag):
                if i < 0 or not(nums):         
                    return 0        
                for j in nums:
                    if i - j == 0:               
                        flag = True
                        return 1
                    else:               
                        b = [foo for foo in nums]
                        b.remove(j)
                        dfs(i - j, b)
            else:      
                return 1

        ans = 0
        for i in range(1,n+1):
            global flag     
            flag = False
            dfs(i, nums)
            if not(flag):
                nums.append(i)
                ans += 1
        return(ans)    

#%% Version 2
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        def dfs(i, nums):
            global flag
            if not(flag):
                if i < 0 or not(nums):         
                    return 0        
                for j in nums:
                    if i - j == 0:               
                        flag = True
                        return 1
                    else:               
                        b = [foo for foo in nums]
                        b.remove(j)
                        dfs(i - j, b)
            else:      
                return 1

        ans = 0
        i = 1
        while(i<=n):
            global flag
            flag = False
            dfs(i, nums)
            if not(flag):
                nums.append(i)
                ans += 1
                i = 2 * i
            else:
                i += 1
        return(ans)    
