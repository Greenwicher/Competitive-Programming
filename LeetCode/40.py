# Version 1, DFS
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(s, l, c):
            if s > target:
                return
            elif s == target:
                ans.append(l)
                return
            else:
                i = 0
                while i < len(c):
                    dfs(s+c[i], l+[c[i]], c[i+1:])
                    j = i + 1
                    while j < len(c) and c[j] == c[i]:
                        j += 1
                    i = j
                return
        ans = []
        candidates = sorted(candidates)
        dfs(0, [], candidates)
        return ans

# Version 2, Dynamic Programming
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        table = [None] + [set() for i in range(target)]
        for i in candidates:
            if i > target:
                break
            for j in range(target - i, 0, -1):
                table[i + j] |= {elt + (i,) for elt in table[j]}
            table[i].add((i,))
        return map(list, table[target])

# Version 3, DFS
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.search(candidates, 0 ,target)

    def search(self, candidates, start, target):
        if target==0:
            return [[]]
        res=[]
        for i in xrange(start,len(candidates)):
            if i!=start and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]>target:
                break
            for r in self.search(candidates, i+1, target-candidates[i]):
                res.append([candidates[i]]+r)
        return res

