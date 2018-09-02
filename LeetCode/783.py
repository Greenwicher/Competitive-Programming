# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 1e100
        queue = [root]
        value = []
        while any(queue):
            q = queue.pop(0)
            if q:
                value.append(q.val)
                queue += [q.left, q.right]
        value = sorted(value)
        for i in range(len(value)-1):
            res = min(res, value[i+1]-value[i])
        return res