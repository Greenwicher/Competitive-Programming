__author__ = 'liuweizhi'

# Version 1, DP, O(N)
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        nums = [0] + nums
        m = len(nums)
        for i in range(1, m):
            nums[i] += nums[i-1]
        self.nums = nums
        return


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        m = len(self.nums)
        i, j = max(i, 0), min(j, m-1)
        return self.nums[j+1] - self.nums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)