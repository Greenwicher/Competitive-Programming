# Version 1
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return [-1, max(len(a), len(b))][a!=b]