# Version 1, Backtracking (check whether can jump over the index of value zero except the last one), O(n^2) time complexity
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans = True
        for i in range(len(nums)-1)[::-1]:
            if nums[i] == 0:
                ans = False
                for j in range(i):
                    if nums[j] > i - j:
                        ans = True
                        break
                if not ans:
                    break
        return ans