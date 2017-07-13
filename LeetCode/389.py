# Version 1
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s, t = sorted(s), sorted(t)
        i = 0
        while i < len(s) and s[i] == t[i]:
            i += 1
        if i < len(s):
            res = t[i]
        else:
            res = t[-1]
        return res