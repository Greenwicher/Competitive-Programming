class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True
        i, j = 0, len(s) - 1
        isPalindrome = lambda x: x == x[::-1]
        while i < j:
            if s[i] != s[j]:
                if isPalindrome(s[i:j]) or isPalindrome(s[i+1:j+1]):
                    return True
                else:
                    return False
            else:
                i += 1
                j -= 1
        return True