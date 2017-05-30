# Version 1, Implementation, O(n^2) time complexity, O(n^2) space complexity
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ans = [[matrix[i][j] for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = ans[n-1-j][i]
        return

# Version 2, see https://discuss.leetcode.com/topic/15295/seven-short-solutions-1-to-7-lines
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = zip(*matrix[::-1])

# Version 3
class Solution:
    def rotate(self, A):
        n = len(A)
        for i in range(n/2):
            for j in range(n-n/2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         A[~j][i], A[~i][~j], A[j][~i], A[i][j]

