# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, Recursion
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            if not(root.left) and not(root.right):
                return root
            left = self.invertTree(root.right)
            right = self.invertTree(root.left)
            root.left, root.right = left, right
        return root