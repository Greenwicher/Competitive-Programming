class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def reduce(num, d):
            while not(num % d):
                num //= d
            return num
        if num == 1:
            return True
        elif num < 1:
            return False
        for d in [2, 3, 5]:
            num = reduce(num, d)
        if num == 1:
            return True
        else:
            return False