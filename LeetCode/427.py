"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        root = Node(None, None, None, None, None, None)
        n = len(grid)
        cnt = sum([grid[i][j] for i in range(n) for j in range(n)])
        if cnt == 0 or cnt == n**2:
            root.val = cnt == n**2
            root.isLeaf = True
        else:
            root.isLeaf = False
            root.val = '*'
            topLeftGrid = [[grid[i][j] for j in range(n//2)] for i in range(n//2)]
            topRightGrid = [[grid[i][j] for j in range(n//2, n)] for i in range(n//2)]
            bottomLeftGrid = [[grid[i][j] for j in range(n//2)] for i in range(n//2, n)]
            bottomRightGrid = [[grid[i][j] for j in range(n//2, n)] for i in range(n//2, n)]
            root.topLeft = self.construct(topLeftGrid)
            root.topRight = self.construct(topRightGrid)
            root.bottomLeft = self.construct(bottomLeftGrid)
            root.bottomRight = self.construct(bottomRightGrid)
        return root