# Version 1, Implementation, O(m*n) time complexity, O(1) space complexity
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for _i in range(m):
                        if matrix[_i][j]:
                            matrix[_i][j] = False
                    for _j in range(n):
                        if matrix[i][_j]:
                            matrix[i][_j] = False
        for i in range(m):
            for j in range(n):
                if type(matrix[i][j]) == bool:
                    matrix[i][j] = 0
        return

# Version 2, Implementation, O(m*n) time complexity, O(1) space complexity
class Solution(object):
    def setZeroes(self, matrix):
        # First row has zero?
        m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
        # Use first row/column as marker, scan the matrix
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        # Set the zeros
        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Set the zeros for the first row
        if firstRowHasZero:
            matrix[0] = [0] * n
        return