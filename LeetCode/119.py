# Version 1, Mathematics Formula, O(n^2) time complexity, O(n) space complexity
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def cnk(n, k):
            f = lambda i: i * f(i-1) if i > 0 else 1
            return f(n) / (f(n-k) * f(k))
        return [cnk(rowIndex, i) for i in range(rowIndex+1)]

# Version 2, Simulation, O(n^2) time complexity, O(n^2) ? space complexity
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
