class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        i, j, v = 1, 1, nums[0]
        while i < len(nums):
            if nums[i] == v:
                if j < 2:
                    j += 1
                    i += 1
                else:
                    del nums[i]
            else:
                v = nums[i]
                j = 1
                i += 1
        return len(nums)