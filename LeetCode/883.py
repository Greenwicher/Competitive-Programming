class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        xy, yz, zx = [0] * 3
        for i in range(m):
            for j in range(n):
                if grid[i][j]: xy += 1
        for i in range(m):
            zx += max([grid[i][j] for j in range(n)])
        for j in range(n):
            yz += max([grid[i][j] for i in range(m)])
        return xy + yz + zx