# Version 1, Two Pointer
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g, s = map(sorted, [g, s])
        i, j, res = [0] * 3
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
            j += 1
        return res
