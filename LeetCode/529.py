__author__ = 'liuweizhi'

# Version 1, BFS
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def bfs(board, click):
            queue = [click]
            m, n = len(board), len(board[0])
            visited = [[False] * n for _ in range(m)]
            import itertools
            directions = list(itertools.product([-1,0,1], repeat=2))
            directions.remove((0, 0))
            while queue:
                x, y = queue.pop(0)
                if not(visited[x][y]):
                    visited[x][y] = True
                    if board[x][y] == 'M':
                        board[x][y] = 'X'
                    else:
                        neighbors = [[x+d[0], y+d[1]] for d in directions if (0 <= x+d[0] <= m-1) and (0 <= y+d[1] <= n-1)]
                        mines = [board[neighbor[0]][neighbor[1]] for neighbor in neighbors].count('M')
                        if mines > 0:
                            board[x][y] = str(mines)
                        else:
                            board[x][y] = 'B'
                            queue.extend(neighbors)
            return board
        return bfs(board, click)
