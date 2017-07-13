# Version 1, Implementation, O(M*N) time complexity
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(findNums)):
            v, flag = -1, False
            for j in range(len(nums)):
                if nums[j] == findNums[i]:
                    flag = True
                if flag and nums[j] > findNums[i]:
                    v = nums[j]
                    break
            res.append(v)
        return v
