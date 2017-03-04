__author__ = 'liuweizhi'

# Version 1, O(N^2)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        nums = [0] + nums
        ans = -1e100
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                ans = max(ans, nums[j] - nums[i])
        return ans

# Version 2, O(N)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        ans = cur = nums[0]
        for i in nums[1:]:
            cur = max(i, cur+i)
            ans = max(ans, cur)
        return ans