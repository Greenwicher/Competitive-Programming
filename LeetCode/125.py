class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([foo.lower() for foo in s if foo.isalnum()])
        return s == s[::-1]