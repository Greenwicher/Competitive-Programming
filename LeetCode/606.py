# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, Recursion
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t:
            left = not(t.left is None)
            right = not(t.right is None)
            if left and right:
                return "%s(%s)(%s)" % (str(t.val), self.tree2str(t.left), self.tree2str(t.right))
            elif left and not(right):
                return "%s(%s)%s" % (str(t.val), self.tree2str(t.left), self.tree2str(t.right))
            elif not(left) and right:
                return "%s(%s)(%s)" % (str(t.val), self.tree2str(t.left), self.tree2str(t.right))
            else:
                return "%s%s%s" % (str(t.val), self.tree2str(t.left), self.tree2str(t.right))
        else:
            return ""
