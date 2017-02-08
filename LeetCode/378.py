#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 23:19:58 2017

@author: liuweizhi
"""

#%% Version 1 Time Limit Exceed
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        leaf = set([(0,0)])
        visited = set([])
        r = 1e100
        while(k):
            v, x, y = 1e100, -1, -1
            for foo in leaf:
                _x, _y = foo
                if matrix[_x][_y] < v:
                    v, x, y = matrix[_x][_y], _x, _y
            r = v      
            leaf.remove((x,y))
            visited.add((x,y))
            if x + 1 < n and not((x+1, y) in visited): leaf.add((x+1, y))
            if y + 1 < n and not((x, y+1) in visited): leaf.add((x, y+1))
            k -=1
        return r
        
        
        
#%% Version 2
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l, r  = matrix[0][0], matrix[-1][-1]
        while (l < r):
            m = (l + r) // 2
            lk, rk = self.rank(m, matrix)
            if lk <= k and k <= rk:
                return m
            elif k < lk:
                r = m
            else:
                l = m + 1
        lk, rk = self.rank(l, matrix)
        if lk <= k and k <= rk:
            return l
        else:
            return -1
            
    def rank(self, m, matrix):
        import bisect
        lk, rk = 1, len(matrix) ** 2
        for foo in matrix:
            lk += bisect.bisect_left(foo, m)
            rk -= len(foo) - bisect.bisect_right(foo, m)
        return lk, rk
        
#matrix = [[1,2,3,7],[5,10,14,16],[8,10,18,19],[9,12,22,24]]
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = len(matrix) ** 2
test = Solution()
for i in range(1, k+1):
    print(i, test.kthSmallest(matrix, i))