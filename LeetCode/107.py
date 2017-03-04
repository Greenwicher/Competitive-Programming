__author__ = 'liuweizhi'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, BFS
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        row = [root]
        while any(row):
            ans.append([r.val for r in row])
            _row, row = row, []
            for r in _row:
                if r.left:
                    row.append(r.left)
                if r.right:
                    row.append(r.right)
        return ans[::-1]