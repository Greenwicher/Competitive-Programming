class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bit = bin(n)[2:]
        for i in range(len(bit)-1):
            if bit[i] == bit[i+1]:
                return False
        return True