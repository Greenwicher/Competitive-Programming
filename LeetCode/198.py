__author__ = 'liuweizhi'

# Version 1, O(N^2)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        dp = [[0]*2 for _ in range(n)]
        dp[0][0], dp[0][1] = 0, nums[0]
        for i in range(1, n):
            for j in range(i):
                dp[i][0] = max([dp[i][0], dp[j][0], dp[j][1]])
            for j in range(i-1):
                dp[i][1] = max([dp[i][1], nums[i]+dp[j][0], nums[i]+dp[j][1]])
            dp[i][1] = max(dp[i][1], nums[i]+dp[i-1][0])
        return max(dp[n-1][0], dp[n-1][1])