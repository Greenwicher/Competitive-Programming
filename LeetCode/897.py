# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def traversal(root):
            if root is not None:
                return traversal(root.left) + [root] + traversal(root.right)
            else:
                return []
        lst = traversal(root)
        for i, v in enumerate(lst[:-1]):
            v.left = None
            v.right = lst[i+1]
        return lst[0]