class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(M), len(M[0])
        N = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                value_neighbor = [M[x+i][y+j] for x,y in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)] if 0<=x+i<m and 0<=y+j<n]
                N[i][j] = sum(value_neighbor) // len(value_neighbor)
        return N