# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, Breadth-first-search, O(N) time complexity, O(logN) space complexity
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue, res = [root], []
        while any(queue):
            v = [foo.val for foo in queue if foo]
            res.append(sum(v) / len(v))
            num = len(queue)
            while num:
                node = queue.pop(0)
                if node:
                    queue += [node.left, node.right]
                num -= 1
        return res