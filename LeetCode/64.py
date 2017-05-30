# Version 1, Dynamic Programming, O(m^n) time complexity, O(m^n) space complexity
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not len(grid) or not len(grid[0]):
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] += dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] += dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]

# Version 2, for more efficient space complexity, please refer to
# https://discuss.leetcode.com/topic/19759/python-solutions-o-m-n-o-n-space/2