# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(root, leaf):
            if root is not None:
                if (root.left is None) and (root.right is None):
                    return leaf + [root.val]
                else:
                    leaf = dfs(root.left, leaf)
                    leaf = dfs(root.right, leaf)
                    return leaf
            else:
                return leaf
        leaf1 = dfs(root1, [])
        leaf2 = dfs(root2, [])
        return leaf1 == leaf2