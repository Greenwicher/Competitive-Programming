__author__ = 'liuweizhi'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, Recursive DFS
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def btp(root, path):
            if root.left is None and root.right is None:
                ans.append(path)
            if root.left:
                btp(root.left, path+"->%d" % root.left.val)
            if root.right:
                btp(root.right, path+"->%d" % root.right.val)
            return
        if root is None:
            return []
        ans = []
        btp(root, "%d" % root.val)
        return ans


# Version 2
def binaryTreePaths(self, root):
    if not root:
        return []
    return [str(root.val) + '->' + path
            for kid in (root.left, root.right) if kid
            for path in self.binaryTreePaths(kid)] or [str(root.val)]
