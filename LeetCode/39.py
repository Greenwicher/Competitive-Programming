# Version 1, DFS
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(s, l):
            if s > target:
                return
            elif s == target:
                ans.append(l)
                return
            else:
                for foo in candidates:
                    if not l or foo <= l[-1]:
                        dfs(s+foo, l+[foo])
                    else:
                        break
        ans = []
        candidates = sorted(candidates)
        dfs(0, [])
        return ans

# Version 2, Dynamic Programming
class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        dp = [[[]]] + [[] for i in xrange(target)]
        for i in xrange(1, target + 1):
            for number in candidates:
                if number > i: break
                for L in dp[i - number]:
                    if not L or number >= L[-1]: dp[i] += L + [number],
        return dp[target]
