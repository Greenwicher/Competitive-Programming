# Version 1, Implementation, O(n) time complexity, O(1) space complexity
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = [0, 1][len(nums) > 0]
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                del nums[i]
            else:
                i += 1
                ans += 1
        return ans