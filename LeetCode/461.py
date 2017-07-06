# Version 1, Base Two and XOR
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        return bin(x^y).count('1')