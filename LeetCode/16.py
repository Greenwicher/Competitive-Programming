# Version 1, Brute Force, O(n^3) time complexity, O(n^3) space complexity
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import itertools
        comb = itertools.combinations(nums, 3)
        diff, ans = 1e100, 0
        for foo in comb:
            if abs(sum(foo) - target) < diff:
                diff = abs(sum(foo) - target)
                ans = sum(foo)
        return ans