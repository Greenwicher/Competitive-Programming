class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        ans, share = 0, 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                if share == 0:
                    share = 1
                    ans -= prices[i]
            elif prices[i+1] < prices[i]:
                if share == 1:
                    share = 0
                    ans += prices[i]
        if share == 1:
            ans += prices[-1]
        return ans