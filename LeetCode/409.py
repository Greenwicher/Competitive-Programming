# Version 1
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        count = Counter(s)
        res, odd = 0, 0
        for k, v in count.items():
            res += v
            odd += v % 2
        return res - odd + 1 * (odd > 0)