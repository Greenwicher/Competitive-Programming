# Version 1, Dynamic Programming, O(m*n) time complexity, O(m*n) space complexity
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = [0, 1][obstacleGrid[0][0] == 0]
        for i in range(1, m):
            dp[i][0] = [dp[i-1][0], 0][obstacleGrid[i][0] == 1]
        for j in range(1, n):
            dp[0][j] = [dp[0][j-1], 0][obstacleGrid[0][j] == 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]