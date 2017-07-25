# Version 1
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        count = Counter(s)
        for i, v in enumerate(s):
            if count[v] == 1:
                return i
        return -1