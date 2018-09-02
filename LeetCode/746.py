class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost = [0] + cost + [0]
        dp = [0] * len(cost)
        for i in range(3):
            dp[i] = 0
        for i in range(3, len(cost)):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]