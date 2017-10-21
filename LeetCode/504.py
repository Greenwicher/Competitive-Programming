# Version 1
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return '0'
        res = []
        a, b = abs(num), 0
        while a:
            a, b = a//7, a%7
            res.append(str(b))
            print(a,b)
        return '-' * (num < 0) + ''.join(res[::-1])

s = Solution()
res = s.convertToBase7(-2333)