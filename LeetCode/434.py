class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum([foo != ' ' for foo in s.split(' ')])