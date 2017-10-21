# Version 1
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digit = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i, v in enumerate(s[:-1]):
            if digit[v] >= digit[s[i+1]]:
                res += digit[v]
            else:
                res -= digit[v]
        return res + digit[s[-1]]