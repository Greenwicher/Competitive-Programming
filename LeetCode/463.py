# Version 1, Enumeration, O(N^2) time complexity
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def perimeter(i, j):
            return 4 - sum([1 for x,y in [(0, -1), (-1, 0), (0, 1), (1, 0)] if 0<=i+x<m and 0<=j+y<n and grid[i][j]])
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res += perimeter(i, j)
        return res