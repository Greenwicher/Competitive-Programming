class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = {0:1} # cum == k
        cum = ans = 0
        for foo in nums:
            cum += foo
            # cum - k, k, cum
            ans += sums.get(cum - k, 0)
            sums[cum] = sums.get(cum, 0) + 1
        return ans