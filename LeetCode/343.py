# Version 1, Dynamic Programming
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n+1)
        for i in range(3, n+1):
            for j in range(1, i//2+1):
                dp[i] = max([dp[i], dp[j]*dp[i-j], dp[j]*(i-j), j*dp[i-j], j*(i-j)])
        return dp[n]


s = Solution