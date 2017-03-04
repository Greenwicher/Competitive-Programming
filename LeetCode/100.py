__author__ = 'liuweizhi'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, Recursice DFS
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p is None) and (q is None):
            return True
        if (p is None) != (q is None):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Version 2, Iterative DFS
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None: return True
        if (p != None) != (q != None): return False
        stackp = [(p, 1)]
        stackq = [(q, 1)]
        flag = True
        while stackp and stackq:
            p, u = stackp.pop()
            q, v = stackq.pop()
            if p.val != q.val or u != v:
                flag = False
                break
            if p.left:
                stackp.append((p.left, u*2))
            if p.right:
                stackp.append((p.right, u*2+1))
            if q.left:
                stackq.append((q.left, v*2))
            if q.right:
                stackq.append((q.right, v*2+1))
        if (stackp != []) != (stackq != []):
            flag = False
        return flag

