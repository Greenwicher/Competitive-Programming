class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(sr, sc):
            image[sr][sc] = newColor
            visited[sr][sc] = True
            for i, j in [(-1,0), (1,0), (0,-1), (0,1)]:
                nsr, nsc = sr+i, sc+j
                if 0<=nsr<m and 0<=nsc<n and image[nsr][nsc] == oldColor and not(visited[nsr][nsc]):
                    dfs(nsr, nsc)
            return
        m, n = len(image), len(image[0])
        visited = [[False] * n for _ in range(m)]
        oldColor = image[sr][sc]
        dfs(sr, sc)
        return image