"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def travel(root, res):
            if root is None:
                return res
            else:
                for children in root.children:
                    res += travel(children, [])
                return res + [root.val]
        return travel(root, [])