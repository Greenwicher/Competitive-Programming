__author__ = 'liuweizhi'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        row = [root]
        while any(row):
            ans.append(row[-1].val)
            _row, row = row, []
            for r in _row:
                if r.left:
                    row.append(r.left)
                if r.right:
                    row.append(r.right)
        return ans