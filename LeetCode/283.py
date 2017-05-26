class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            if not(nums[i]):
                j = i + 1
                while j < len(nums) and not(nums[j]):
                    j += 1
                if j != len(nums):
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
        return