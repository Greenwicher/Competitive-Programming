class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def combinations(work, left, k):
            if k == 0:
                global comb
                comb.append(work)
            else:
                for foo in left:
                    if not work or foo > work[-1]:
                        tmp = [bar for bar in left if bar != foo]
                        combinations(work+[foo], tmp, k - 1)
            return
        global comb
        comb, ans = [], []
        combinations([], list(range(1, 10)), k)
        for foo in comb:
            if sum(foo) == n:
                ans.append(foo)
        return ans

# Version 2
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        output = []
        stack = [(0, 1, [])]
        while stack:
            total, start, comb = stack.pop()
            if total == n and len(comb) == k:
                output.append(comb)
                continue

            for num in range(start, 10):
                tmp_total = total + num
                if tmp_total > n:
                    break
                stack.append((tmp_total, num + 1, comb + [num]))
        return output
