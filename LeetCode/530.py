# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, BFS
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        v = []
        queue = [root]
        while any(queue):
            v += [foo.val for foo in queue if foo]
            num = len(queue)
            while num:
                q = queue.pop(0)
                if q: queue += [q.left, q.right]
                num -= 1
        v = sorted(v)
        res = 1e100
        for i in range(len(v)-1):
            res = min(abs(v[i+1]-v[i]), res)
        return res
