# Version 1
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        f = lambda x: sum(map(int, str(x)))
        while len(str(f(num))) != 1:
            num = f(num)
        return f(num)