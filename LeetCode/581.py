# Version 1, Sorting, O(nlogn) time complexity, O(n) space complexity
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _nums = sorted(nums)
        i, j = 0, len(nums) - 1
        while i < len(nums) and nums[i] == _nums[i]:
            i += 1
        while j > 0 and nums[j] == _nums[j]:
            j -= 1
        return [j-i+1, 0][j<=i]