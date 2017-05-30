# Version 1, Implementation, O(n^2) time complexity, O(n^2) space complexity
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numsRows == 0:
            return [[]]
        ans = [[1]]
        if numRows == 1:
            return ans
        for i in range(1, numRows):
            tmp = []
            for j in range(i):
                tmp += [ans[i-1][j] + ans[i-1][j+1]]
            ans.append([1] + tmp + [1])
        return ans

# Version 2, Nice Implementation based on map()
class Solution(object):
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
