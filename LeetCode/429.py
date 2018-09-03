"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        level = [root]
        while any(level):
            next_level = []
            curr_res = []
            for foo in level:
                if foo:
                    curr_res.append(foo.val)
                    next_level += foo.children
            res.append(curr_res)
            level = next_level
        return res