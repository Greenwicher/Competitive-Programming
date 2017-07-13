# Version 1, Recursion, Memory limit exceeded
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse = lambda x: x[-1] + reverse(x[:-1]) if len(x) > 1 else x
        return reverse(s)

# Version 2, Straightforward Implementation
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

# Version 3, Recursion with Divide and Conquer
class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])

