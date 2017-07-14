# Version 1
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        a, b = 1e100, 1e100
        for _a, _b in ops:
            a = min(a, _a)
            b = min(b, _b)
        return a * b