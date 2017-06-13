# Version 1, Greedy, O(n) time complexity, O(1) space complexity
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not flowerbed: return False
        m, l = len(flowerbed), 0
        for i in range(m):
            if not flowerbed[i]:
                lflag, rflag = False, False
                if (i-1 >= 0 and not flowerbed[i-1]) or (i==0): lflag = True
                if (i+1 < m and not flowerbed[i+1]) or (i==m-1): rflag = True
                if lflag and rflag:
                    flowerbed[i] = 1
                    l += 1
        return l >= n