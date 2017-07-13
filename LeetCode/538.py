# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, Depth First Search
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        v, queue = [], [root]
        while any(queue):
            v += [foo.val for foo in queue if foo]
            num = len(queue)
            for i in range(num):
                node = queue.pop(0)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        v = sorted(v)
        dict_v, cum_v = {}, 0
        for i in range(len(v))[::-1]:
            dict_v[v[i]] = cum_v
            cum_v += v[i]
        queue = [root]
        while any(queue):
            for foo in queue:
                if foo:
                    foo.val += dict_v[foo.val]
            num = len(queue)
            for i in range(num):
                node = queue.pop(0)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        return root
