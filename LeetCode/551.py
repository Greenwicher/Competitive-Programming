# Version 1
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c1 = s.count('A') > 1
        c2 = s.count('LLL') > 0
        return not(c1 or c2)