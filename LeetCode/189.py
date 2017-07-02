# Version 1, Simulation, O(N*K) time complexity (TLE), O(1) space complexity
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            a = nums[-1]
            for i in range(len(nums)):
                b = nums[i]
                nums[i] = a
                a = b
        return


# Version 2, O(N) time complexity, O(N) space complexity
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-k:] + nums[:len(nums)-k]
        return

# Version 3, O(N) time complexity, O(1) space complexity
# Classical 3-step array rotation:
# 1. reverse the first n - k elements
# 2. reverse the rest of them
# 3. reverse the entire array
class Solution(object):
    def rotate(self, nums, k):
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1


# Version 4, see https://discuss.leetcode.com/topic/47235/summary-of-solutions-in-python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n, k, j = len(nums), k % len(nums), 0
        while n > 0 and k % n != 0:
            for i in xrange(0, k):
                nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i] # swap
            n, j = n - k, j + k
            k = k % n