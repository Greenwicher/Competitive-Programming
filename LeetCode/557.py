# Version 1, Implementation
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(map(lambda x: x[::-1], s.split(' ')))

# Version 2, Implementation
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse = lambda x: x[-1] + reverse(x[:-1]) if len(x) > 1 else x
        return ' '.join(map(reverse, s.split(' ')))
