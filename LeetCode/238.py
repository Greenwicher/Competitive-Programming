#Version 1, O(N) time without division, O(N) space
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        left, right = [[1] * (size+1) for _ in range(2)]
        for i in range(size):
            left[i+1] *= left[i] * nums[i]
            right[size-i-1] *= right[size-i] * nums[size-i-1]
        ans = []
        for i in range(size):
            ans.append(left[i] * right[i+1])
        return ans

#Version 2, O(N) time without division, O(1) space
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
