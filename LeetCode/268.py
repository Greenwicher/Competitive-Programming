class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, flag = len(nums), True
        for i in range(n):
            if abs(nums[i]) != n:
                nums[abs(nums[i])] *= -1
            else:
                flag = False
        if flag:
            return n
        for i in range(len(nums)):
            if nums[i] > 0:
                return i
        for i in range(len(nums)):
            if nums[i] == 0:
                return i

# version 2
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        return n*(n+1)/2-sum(nums)

# version 3
class Solution(object):
    def missingNumber(self, nums):
        xor = 0
        for i, e in enumerate(nums):
            xor = xor ^ i ^ e
        return xor ^ len(nums)
