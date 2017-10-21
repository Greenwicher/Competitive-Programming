# Version 1
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import Counter
        res = 0
        for x1, y1 in points:
            dist = [abs(x1-x2)**2 + abs(y1-y2)**2 for x2, y2 in points]
            count = Counter(dist)
            res += sum([v*(v-1) for v in count.values()])
        return res