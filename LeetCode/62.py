# Version 1, DP, O(m*n) time
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            return dp[m-1][n-1]

# Version 2, Math Formula, O(1) time
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = lambda x: f(x-1) * x if x > 0 else 1
        return f(m+n-2) / (f(m-1) * f(n-1))