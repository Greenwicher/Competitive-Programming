class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1-A[i][-j-1] for j in range(len(A[i]))] for i in range(len(A))]