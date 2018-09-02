# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        res = set()
        while any(queue):
            _queue = []
            for q in queue:
                if q:
                    res.add(q.val)
                    _queue += [q.left, q.right]
            queue = _queue
        if len(res) > 1:
            return sorted(res)[1]
        else:
            return -1