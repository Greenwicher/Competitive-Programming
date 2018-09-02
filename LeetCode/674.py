class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        res, length = 0, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                length += 1
            else:
                res = max(res, length)
                length = 1
        res = max(res, length)
        return res