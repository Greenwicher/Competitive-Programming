class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        from collections import  defaultdict
        seen = defaultdict(int)
        while 1:
            seen[n] = 1
            digit = list(map(int, str(n)))
            square_sum = sum([d**2 for d in digit])
            if square_sum == 1:
                return 1
            n = int(''.join(map(str, digit)))
            if seen[n]:
                return 0