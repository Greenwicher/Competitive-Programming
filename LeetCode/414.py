# Version 1, Sorting, O(NlogN) time complexity, O(1) space complexity
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums), reverse=True)
        if len(nums) > 2:
            return nums[2]
        else:
            return nums[0]

# Version 2, Enumerating, O(N) time complexity, O(1) space complexity
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = [-1e100]
        for foo in set(nums):
            i = 0
            while i < 3 and i < len(ans):
                if foo < ans[i]:
                    i += 1
                else:
                    ans = ans[:i] + [foo] + ans[i:3]
                    break
        if len(set(nums)) > 2:
            return ans[2]
        else:
            return ans[0]
