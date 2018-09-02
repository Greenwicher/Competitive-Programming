"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def dfs(root, depth):
            if root is None:
                return depth
            else:
                return max([dfs(children, depth+1) for children in root.children]+[depth+1])
        return dfs(root, 0)