__author__ = 'liuweizhi'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, Iterative DFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [(root, 1)]
        ans = 0
        while stack:
            v, l = stack.pop()
            if v.left is None and v.right is None:
                ans = max(ans, l)
            if v.left:
                stack.append((v.left, l+1))
            if v.right:
                stack.append((v.right, l+1))
        return ans

# Version 2, Recursive DFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1 + max(map(self.maxDepth, [root.right, root.left])) if root else 0