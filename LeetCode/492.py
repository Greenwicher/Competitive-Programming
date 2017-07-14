# Version 1
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        L = -int(-area**.5//1)
        while L <= area:
            if not(area % L):
                return [L, area/L]
            else:
                L += 1