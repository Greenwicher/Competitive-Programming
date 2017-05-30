# Version 1, Two Pointers, O(n) time complexity
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, n = 0, len(nums)
        p, q = 0, n - 1
        while i < q + 1:
            if nums[i] == 1:
                i += 1
                continue
            if nums[i] == 0:
                nums[p], nums[i] = nums[i], nums[p]
                if i == p:
                    i += 1
                p += 1
            if nums[i] == 2:
                nums[q], nums[i] = nums[i], nums[q]
                if i == q:
                    i += 1
                q -= 1
            print(i, nums)
        return

# Version 2, see also https://www.wikiwand.com/en/Dutch_national_flag_problem,
# https://discuss.leetcode.com/topic/26181/ac-python-in-place-one-pass-solution-o-n-time-o-1-space-no-swap-no-count/2
def sortColors(self, nums):
    i = j = 0
    for k in range(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1
