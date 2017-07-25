# Version 1
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for foo in s:
            res = res * 26 + ord(foo) - ord('A') + 1
        return res