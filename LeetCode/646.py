# Version 1, Wrong Understanding
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        n = len(pairs)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] + 1 * (pairs[j][1] < pairs[i][0]))
        return dp[-1]


# Version 2, Greedy
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        cur, res = -1e100, 0
        for p in sorted(pairs, key = lambda x: x[1]):
            if cur < p[0]: cur, res = p[1], res + 1
        return res

# Version 3, Dynamic Programming
# see https://discuss.leetcode.com/topic/97999/python-solution-with-detailed-explanation
class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key = lambda x:(x[0], x[1]))
        LIS = [1]*len(pairs)
        for i in range(1, len(pairs)):
            for j in range(i):
                LIS[i] = max(LIS[i], LIS[j]+1) if pairs[j][1] < pairs[i][0] else LIS[i]
        return LIS[-1]