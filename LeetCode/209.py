# Version 1, Dynamic Programming and Bineary Search, O(nlogn) time complexity, O(1) space complexity
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        minLength, nums, flag = 1e100, [0] + nums, False
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        for i in range(1, len(nums)):
            j = bisect.bisect_left(nums, s + nums[i-1])
            if j != len(nums) and j - i + 1 < minLength:
                minLength = j - i + 1
                flag = True
        return [0, minLength][flag]


# Version 2, Two Pointer, O(n) time complexity, O(1) space complexity
class Solution:
    def minSubArrayLen(self, s, nums):
        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0