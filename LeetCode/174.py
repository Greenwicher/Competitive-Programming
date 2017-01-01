#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 18:48:20 2016

@author: liuweizhi
"""

#%% Version 1 Wrong Answer
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        f = [[-1] * n for i in range(m)]
        g = [[-1] * n for i in range(m)]
        # initialize the starting point
        f[0][0] = max(1 - dungeon[0][0], 1)
        g[0][0] = max(1, dungeon[0][0] + 1)
        # initialize the first column
        for i in range(1, m):
            f[i][0] = f[i-1][0] + max(1 - g[i-1][0] - dungeon[i][0], 0)
            g[i][0] = max(1, dungeon[i][0] + g[i-1][0])
        # initialize the first row
        for j in range(1, n):
            f[0][j] = f[0][j-1] + max(1 - g[0][j-1] - dungeon[0][j], 0)
            g[0][j] = max(1, dungeon[0][j] + g[0][j-1])
        # solve for other states
        for i in range(1, m):
            for j in range(1, n):
                v1 = f[i-1][j] + max(1 - g[i-1][j] - dungeon[i][j], 0)
                v2 = f[i][j-1] + max(1 - g[i][j-1] - dungeon[i][j], 0)
                f[i][j] = min(v1, v2)
                if v1 < v2:
                    g[i][j] = max(1, dungeon[i][j] + g[i-1][j])
                elif v2 < v1:
                    g[i][j] = max(1, dungeon[i][j] + g[i][j-1])
                else:
                    g[i][j] = max(1, dungeon[i][j] + g[i-1][j], dungeon[i][j] + g[i][j-1])
        print('f', f)
        print('g', g)
        return f[m-1][n-1]

solver = Solution()
dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
solver.calculateMinimumHP(dungeon)

#%% Version 2 
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        f = [[-1] * n for i in range(m)]
        f[m-1][n-1] = max(1 - dungeon[m-1][n-1], 1)
        # initialize the last column
        for i in range(m-1)[::-1]:
            f[i][n-1] = max(f[i+1][n-1] - dungeon[i][n-1], 1)
        # initialize the last row
        for j in range(n-1)[::-1]:
            f[m-1][j] = max(f[m-1][j+1] - dungeon[m-1][j], 1)
        # solve for other states from the second last row and the second last column
        for i in range(m-1)[::-1]:
            for j in range(n-1)[::-1]:
                f[i][j] = max(min(f[i+1][j], f[i][j+1]) - dungeon[i][j], 1)
        return f[0][0]

solver = Solution()
#dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
#dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
#dungeon = [[2,1],[1,-1]]
dungeon = [[10,4,-48,-8,-87,9],[49,-100,6,-15,41,-99],[-76,-45,-26,50,46,14],[-81,-92,46,-62,-26,1],[-44,19,26,-98,-49,-72]]
solver.calculateMinimumHP(dungeon)