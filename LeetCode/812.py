class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(i, j, k):
            vec1 = (j[0]-i[0], j[1]-i[1])
            vec2 = (k[0]-i[0], k[1]-i[1])
            len1 = distance(i, j) ** 2
            len2 = (inner_product(vec1, vec2) / distance(i, k)) ** 2
            if abs(len1-len2) < 1e-8:
                res = 0
            else:
                h = (len1 - len2) ** 0.5
                d = distance(i, k)
                res = 0.5 * d * h
            return res

        def inner_product(i, j):
            return i[0] * j[0] + i[1] * j[1]

        def distance(i, j):
            return ((i[0]-j[0])**2 + (i[1]-j[1])**2) ** 0.5

        num = len(points)
        comb = [(points[i], points[j], points[k]) for i in range(num) for j in range(i+1, num) for k in range(j+1, num)]
        res = 0
        for i, j, k in comb:
            res = max(res, area(i, j, k))
        return res

s = Solution()
s.largestTriangleArea([[2,5],[7,7],[10,8],[10,10],[1,1]])