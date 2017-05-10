class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] *= -1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]

print(Solution().findDisappearedNumbers([4,3,2,7,7,2,3,1]))