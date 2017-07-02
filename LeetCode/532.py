# Version 1, Meet-in-the-Middle, O(N) time complexity, O(N) space complexity
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        import collections
        dict_nums = collections.Counter(nums)
        for foo in set(nums):
            if k == 0:
                if dict_nums[foo] > 1:
                    ans += 1
            elif k > 0:
                if dict_nums[foo+k]:
                    ans += 1
        return ans