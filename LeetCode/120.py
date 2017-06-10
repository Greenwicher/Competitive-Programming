# Version 1, Dynamic Programming, O(n) time complexity, O(1) space complexity
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        n = len(triangle)
        for i in range(n-1)[::-1]:
            for j in range(i+1):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

# Version 2, DP, one-liner
class Solution(object):
    def minimumTotal(self, t):
        return reduce(lambda a, b: [f + min(d, e) for d, e, f in zip(a, a[1:], b)], t[::-1])[0]


# Version 3, DP, O(n) time, O(n) space
class Solution(object):
    def minimumTotal(self, triangle):
        f = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in xrange(len(row)):
                f[i] = row[i] + min(f[i], f[i + 1])
        return f[0]

