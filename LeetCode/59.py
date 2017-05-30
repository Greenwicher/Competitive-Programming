# Version 1, Simulation, O(n^2) time complexity
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0] * n  for _ in range(n)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count, count_d = 0, 0
        i, j = 0, -1
        while count < n * n:
            d1, d2 = direction[count_d % 4]
            i += d1
            j += d2
            while 0 <= i < n and 0 <= j < n and ans[i][j] == 0:
                ans[i][j] = count + 1
                count += 1
                i += d1
                j += d2
            i -= d1
            j -= d2
            count_d += 1
        return ans


# Version 2, inside-out
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A, lo=[],n*n+1
        while lo>1:
            lo,hi=lo-len(A),lo
            A=[range(lo,hi)]+zip(*A[::-1])
        return A

# Version 3, Similar with Version 1 but much simpler
class Solution(object):
    def generateMatrix(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in xrange(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A
