__author__ = 'liuweizhi'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, TLE, BFS
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        row = [root]
        flag = True
        while any(row):
            ans = []
            for r in row:
                if not r:
                    ans.append(None)
                else:
                    ans.append(r.val)
            flag = ans == ans[::-1]
            if not flag:
                break
            _row, row = row, []
            for r in _row:
                if not r:
                    row.extend([None, None])
                else:
                    row.extend([r.left, r.right])
        return flag

# Version 2, Two-way BFS
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        row = [(root, 0)]
        flag = True
        level = 0
        while row:
            i, j = 0, len(row) - 1
            while i <= j:
                if not(row[i][0].val == row[j][0].val and row[i][1] + row[j][1] == 2 ** level - 1):
                    flag = False
                    break
                i += 1
                j -= 1
            if not flag:
                break
            _row, row = row, []
            for r in _row:
                if r[0].left:
                    row.append((r[0].left, r[1]*2))
                if r[0].right:
                    row.append((r[0].right, r[1]*2+1))
            level += 1
        return flag