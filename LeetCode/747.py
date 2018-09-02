class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        maxnum = [0, 0]
        key = -1
        for i, v in enumerate(nums):
            if v > maxnum[0]:
                maxnum = [v, maxnum[0]]
                key = i
            elif v > maxnum[1]:
                maxnum[1] = v
        if maxnum[0] >= 2*maxnum[1]:
            return key
        return -1