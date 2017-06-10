# Version 1, Construction and Elimination
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        res = [[]]
        nums.sort()
        for item in nums:
            res += [x + [item] for x in res]
        ans = []
        for foo in res:
            flag = True
            for bar in ans:
                if bar == foo:
                    flag = False
                    break
            if flag:
                ans.append(foo)
        return ans


# Version 2
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res


# Version 3
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, nums):
        res = [[]]
        nums.sort()
        for num in nums:
            res += [i + [num] for i in res if i + [num] not in res]
        return res
