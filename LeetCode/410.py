#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:09:13 2017

@author: liuweizhi
"""

#%% Version 1 - Dynamic Programming, O(MN^3), TLE
# d[i][j][k] represents the optima value given ith - jth (included) nums and k
# partition
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        nums = [0] + nums
        n = len(nums)        
        for i in range(n-1):
            nums[i+1] += nums[i] 
        dp = [[[1e100] * (m+1) for _ in range(n)] for _ in range(n)]
        for i in range(1, n):
            for j in range(i, n):
                dp[i][j][1] = nums[j] - nums[i-1]
        for k in range(2, m+1):
            for i in range(1, n-k+1):
                for j in range(k+i-1, n):
                    for l in range(i, j-k+2):
                        # it seems this bellman equation is not complete for possible sub "k"
                        dp[i][j][k] = min(dp[i][j][k], max(dp[i][l][1], dp[l+1][j][k-1])) 
        return dp[1][n-1][m]
        
test = Solution()
test.splitArray([7,2,5,10,8],5)


#%% Version 2 - Dynamic Programming with Binary Search, O(MN^2logN), WA
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        nums = [0] + nums
        n = len(nums)        
        for i in range(n-1):
            nums[i+1] += nums[i] 
        dp = [[[1e100] * (m+1) for _ in range(n)] for _ in range(n)]
        for i in range(1, n):
            for j in range(i, n):
                dp[i][j][1] = nums[j] - nums[i-1]
        for k in range(2, m+1):
            for i in range(1, n-k+1):
                for j in range(k+i-1, n):  
                    # it seems the bellman equation behind is not complete for possible sub "k"
                    # here, I only consider 1 and k-1, possible need enumerate all t and k -t                     
                    f = lambda mm: max(dp[i][mm][1], dp[mm+1][j][k-1])
                    if i == j - k + 1:
                        dp[i][j][k] = f(i)                
                        continue
                    l, r = i, j - k
                    while l != r:
                        mm = (l + r) // 2
                        if f(mm) <= f(mm+1):
                            r = mm
                        else:
                            l = mm + 1
                    if f(l) <= f(l+1):
                        dp[i][j][k] = f(l)  
                    else:
                        dp[i][j][k] = f(l+1)                                          
        return dp[1][n-1][m]
        
test = Solution()
test.splitArray([7,2,5,10,8],5)

#%% Version 3