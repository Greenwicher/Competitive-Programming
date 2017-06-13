# Version 1, Combinations and Bisection and Triangles, O(n^2 * logn) time complexity, O(n^2) space complexity
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        nums = sorted([foo for foo in nums if foo])
        comb = [(i, j) for i in range(len(nums)) for j in range(len(nums)) if i < j]
        ans = 0
        for i, j in comb:
            a, b = nums[i], nums[j]
            lb, ub = abs(a-b), a+b
            l, r = bisect.bisect_right(nums, lb), bisect.bisect_left(nums, ub)
            ans += r - l - 1 * (l <= i < r) - 1 * (l <= j < r)
        return ans // 3

# Version 2, Two Pointer, O(n^2) time complexity, O(1) space complexity
class Solution(object):
    def triangleNumber(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        final = 0
        nums = sorted(nums)
        for i in range(2, len(nums))[::-1]:
            l = 0
            r = i - 1
            while (r > l):
                if nums[l] + nums[r] > nums[i]:
                    final += r - l # given fixed i, r, the possible number of l such that nums[l] + nums[r] > nums[i]
                    r -= 1
                else:
                    l += 1
        return final
