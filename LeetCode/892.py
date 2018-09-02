class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        if (0 <= i+x < n) and (0 <= j+y < n):
                            res += max(grid[i][j] - grid[i + x][j + y], 0)
                        else:
                            res += grid[i][j]
                    res += 2
        return res