class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = [1, -1][x<0]
        res = sign * int(str(abs(x))[::-1])
        if -0x80000000 <= res <= 0x7fffffff:
            return res
        return 0