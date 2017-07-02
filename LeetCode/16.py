# Version 1, Brute Force, O(n^3) time complexity, O(n^3) space complexity
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import itertools
        comb = itertools.combinations(nums, 2)
        diff, ans = 1e100, 0
        for foo in comb:
            if abs(sum(foo) - target) < diff:
                diff = abs(sum(foo) - target)
                ans = sum(foo)
        return ans


# Version 2, Two pointer, O(N^3) time complexity, O(1) space complexity
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = sum((nums[i], nums[l], nums[r]))
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:  # break early
                    return res
        return res