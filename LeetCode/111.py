__author__ = 'liuweizhi'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        row = [root]
        while any(row):
            ans += 1
            leaf = False
            for r in row:
                if r.left is None and r.right is None:
                    leaf = True
                    break
            if leaf:
                break
            _row, row = row, []
            for r in _row:
                if r.left:
                    row.append(r.left)
                if r.right:
                    row.append(r.right)
        return ans