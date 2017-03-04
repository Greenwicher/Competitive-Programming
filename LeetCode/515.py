__author__ = 'liuweizhi'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, BFS
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue, ans = [(root, 0)], []
        level, maxv = 0, -1e100
        while queue:
            node = queue.pop(0)
            if node[1] == level:
                maxv = max(node[0].val, maxv)
            else:
                ans.append(maxv)
                level += 1
                maxv = node[0].val
            if node[0].left:
                queue.append((node[0].left, node[1]+1))
            if node[0].right:
                queue.append((node[0].right, node[1]+1))
        ans.append(maxv)
        return ans