class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0]
        while n:
            res.append(n % 2)
            n //= 2
        return sum(res)