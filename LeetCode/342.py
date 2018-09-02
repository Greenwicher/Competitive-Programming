class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while not(num % 4) or (num==1):
            if num == 1:
                return True
            else:
                num //= 4
        return False