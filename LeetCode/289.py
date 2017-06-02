# Version 1, Implementation with extra space, O(m*n) time complexity, O(m*n) space complexity
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def numLive(i, j):
            neighbors = [(i + x, j + y) for x in (-1, 0, 1) for y in (-1, 0, 1) if (x, y) != (0, 0) and 0 <= i + x < m and 0 <= j + y < n]
            count = 0
            for x, y in neighbors:
                count += board[x][y] == 1
            return count
        m, n = len(board), len(board[0])
        _board = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count = numLive(i, j)
                if board[i][j]:
                    if count < 2 or count > 3:
                        _board[i][j] = 0
                    else:
                        _board[i][j] = 1
                elif count == 3:
                    _board[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = _board[i][j]
        return

# Version 2, Implementation without extra space, O(m*n) time complexity, O(1) space complexity
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def numLive(i, j):
            neighbors = [(i + x, j + y) for x in (-1, 0, 1) for y in (-1, 0, 1) if (x, y) != (0, 0) and 0 <= i + x < m and 0 <= j + y < n]
            count = 0
            for x, y in neighbors:
                count += board[x][y] in (1, 3)
            return count
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = numLive(i, j)
                if board[i][j]:
                    if count < 2 or count > 3:
                        board[i][j] = 3
                elif count == 3:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 1
                if board[i][j] == 3: board[i][j] = 0
        return

