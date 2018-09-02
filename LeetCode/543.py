# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def diameter(root):
            if root is None:
                return 0
            else:
                return max([diameter(root.left), diameter(root.right), 2+depth(root.left)+depth(root.right)])

        def depth(root):
            if root in d:
                return d[root]
            else:
                if root is None:
                    return 0
                else:
                    d[root] = max([depth(root.left), depth(root.right)]) + 1
                    return d[root]
        d = {}
        return diameter(root)
