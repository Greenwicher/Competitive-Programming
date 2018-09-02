class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = {}
        for foo in nums:
            if foo in cnt:
                cnt[foo] += 1
            else:
                cnt[foo] = 1
        pair = sorted([(k, v) for k, v in cnt.items()], key=lambda x: x[0])
        res = 0
        for i in range(len(pair)-1):
            if pair[i+1][0] - pair[i][0] == 1:
                res = max(res, pair[i+1][1] + pair[i][1])
        return res