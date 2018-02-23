class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right+1):
            flag = True
            a, b = num // 10, num % 10
            while a or b:
                if not(b and not(num % b)):
                    flag = False
                    break
                a, b = a // 10, a % 10
            if flag:
                res.append(num)
        return res