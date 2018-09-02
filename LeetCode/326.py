class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        while 3 ** i <= n:
            if 3 ** i == n:
                return True
            else:
                i += 1
        return False