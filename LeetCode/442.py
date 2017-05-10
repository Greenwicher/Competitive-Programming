# Version 1, O(NlogN) time, O(N) space
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                ans.append(nums[i])
        return ans
# Version 2, O(N) time, O(N) space
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1] *= -1
        return ans