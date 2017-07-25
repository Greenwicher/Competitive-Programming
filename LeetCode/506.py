# Version 1
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dict, res = {}, []
        _nums = sorted(nums, reverse=True)
        for i in range(len(_nums)):
            dict[_nums[i]] = i + 1
        for num in nums:
            if dict[num] == 1:
                res.append("Gold Medal")
            elif dict[num] == 2:
                res.append("Silver Medal")
            elif dict[num] == 3:
                res.append("Bronze Medal")
            else:
                res.append(str(dict[num]))
        return res