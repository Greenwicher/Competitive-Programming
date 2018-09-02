class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            mod = n % 26
            if mod:
                res += chr(ord('A') + mod)
                n = n // 26
            else:
                res += 'Z'
                n = n - 1
        return res[::-1]