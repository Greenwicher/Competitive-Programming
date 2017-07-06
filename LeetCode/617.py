# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, Recursion, O(N) time complexity
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def recursive(root, t1, t2):
            # both t1 and t2 are not None
            # merge the node of t1 and t2 to root node
            root.val = t1.val + t2.val
            # construct the left binary tree
            if t1.left or t2.left:
                root.left = TreeNode(0)
            if t1.left and t2.left:
                recursive(root.left, t1.left, t2.left)
            elif t1.left:
                root.left = t1.left
            elif t2.left:
                root.left = t2.left
            # construct the right binary tree
            if t1.right or t2.right:
                root.right = TreeNode(0)
            if t1.right and t2.right:
                recursive(root.right, t1.right, t2.right)
            elif t1.right:
                root.right = t1.right
            elif t2.right:
                root.right = t2.right
            return
        if t1 is None and t2 is None:
            return None
        elif not(t1 is None) and not(t2 is None):
            root = TreeNode(0)
            recursive(root, t1, t2)
            return root
        elif t1 is None:
            return t2
        elif t2 is None:
            return t1


# Version 2
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2: return None
        if t1:
            v1, L1, R1 = t1.val, t1.left, t1.right
        else:
            v1, L1, R1 = 0, None, None
        if t2:
            v2, L2, R2 = t2.val, t2.left, t2.right
        else:
            v2, L2, R2 = 0, None, None
        node = TreeNode(v1+v2)
        node.left = self.mergeTrees(L1, L2)
        node.right = self.mergeTrees(R1, R2)
        return node

# Version 3
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans