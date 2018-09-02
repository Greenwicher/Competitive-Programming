class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        sum = 0
        for i in range(1, int(num**0.5)+1):
            if not(num % i):
                j = num // i
                if j == num or i == j:
                    sum += i
                else:
                    sum += i + j
        if sum == num:
            return True
        else:
            return False