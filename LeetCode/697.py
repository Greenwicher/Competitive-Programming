class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        count = Counter(nums)
        degree, num = 0, []
        for k, v in count.items():
            if v > degree:
                degree = v
                num = [k]
            elif v == degree:
                num.append(k)
        position = {}
        for i, v in enumerate(nums):
            if v in position:
                position[v][1] = i
            else:
                position[v] = [i, i]
        res = 1e100
        for foo in num:
            res = min(res, position[foo][1]-position[foo][0]+1)
        return res