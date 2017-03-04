__author__ = 'liuweizhi'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None: return False
        stack = [(root, root.val)]
        flag = False
        while stack:
            r, v = stack.pop()
            if r.left is None and r.right is None:
                flag = v == sum
            if flag:
                break
            if r.left:
                stack.append((r.left, v+r.left.val))
            if r.right:
                stack.append((r.right, v+r.right.val))
        return flag