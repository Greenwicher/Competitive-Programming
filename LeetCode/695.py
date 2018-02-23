class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]:
                    _res = 0
                    queue = [(i, j)]
                    while any(queue):
                        _queue = []
                        for p, q in queue:
                            if not visited[p][q] and grid[p][q]:
                                _res += 1
                                visited[p][q] = True
                                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                    if 0<=p+x<m and 0<=q+y<n and not visited[p+x][q+y]:
                                        _queue.append((p+x, q+y))
                        queue = _queue
                    res = max(res, _res)
        return res





def maxAreaOfIsland(self, grid):
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if 0 <= i < m and 0 <= j < n and grid[i][j]:
            grid[i][j] = 0
            return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
        return 0

    areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
    return max(areas) if areas else 0