# Version 1, Bitwise Not
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join([str(1-int(foo)) for foo in bin(num)[2:]]), 2)

# Version 2, Bitwise XOR
class Solution(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num
