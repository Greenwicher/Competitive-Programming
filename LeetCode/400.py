class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while n > 9 * (10 ** (i-1)) * i:
            n -= 9 * (10 ** (i-1)) * i
            i += 1
        a = -(- n // i)
        b = n % i
        c = 10 ** (i-1) + a
        return int(str(c)[b-1])