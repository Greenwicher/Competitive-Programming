__author__ = 'liuweizhi'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, BFS
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q, _q = [(root, 0)], []
        while q:
            if q[0][0].left:
                q.append((q[0][0].left, q[0][1]+1))
            if q[0][0].right:
                q.append((q[0][0].right, q[0][1]+1))
            _q.append(q.pop(0))
        for foo in _q[::-1]:
            if foo[1] != _q[-1][1]:
                break
            ans = foo[0]
        return ans

# Version 2, BFS (Right to Left)
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val

# Version 3, DFS
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q, _q = [(root, 0)], []
        maxlevel = 0
        while q:
            v = q.pop()
            _q.append(v)
            if v[0].right:
                q.append((v[0].right, v[1]+1))
            if v[0].left:
                q.append((v[0].left, v[1]+1))
            maxlevel = max(maxlevel, v[1])
        for foo in _q:
            if foo[1] == maxlevel:
                ans = foo[0].val
                break
        return ans