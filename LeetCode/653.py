# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        from collections import defaultdict
        num = defaultdict(int)
        queue = [root]
        while any(queue):
            _queue = []
            for q in queue:
                if q:
                    num[q.val] += 1
                    _queue += [q.left, q.right]
            queue = _queue
        num_iteritems = [(key, value) for key, value in num.iteritems()]
        for key, value in num_iteritems:
            if num[k-key]:
                if (k == 2*key and num[key] > 1) or (k != 2*key):
                    return True
        return False