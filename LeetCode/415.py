# Version 1
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2, res = num1[::-1], num2[::-1], ''
        i, a = [0] * 2
        while i < len(num1) or i < len(num2):
            try:
                x = int(num1[i])
            except:
                x = 0
            try:
                y = int(num2[i])
            except:
                y = 0
            a, b = (x+y+a)//10, (x+y+a)%10
            res += str(b)
            i += 1
        if a:
            res += str(a)
        print(int(num1[::-1])+int(num2[::-1])-int(res[::-1]))
        return res[::-1]

s = Solution()
s.addStrings('1022345499999999', '78983497749009999999')
s.addStrings('1', '9')
