__author__ = 'liuweizhi'

# Version 1, DP, O(N)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        ans, low = 0, prices[0]
        for p in prices[1:]:
            ans = max(ans, p-low)
            low = min(low, p)
        return ans