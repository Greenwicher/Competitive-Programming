__author__ = 'liuweizhi'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, Recursive DFS
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        depth = {None: 0,}
        flag = True
        def dfs(root):
            if not flag:
                return False
            if root is None: return True
            if root.left is None and root.right is None:
                depth[root] = 1
                return True
            dfs(root.left)
            dfs(root.right)
            depth[root] = max(depth[root.left], depth[root.right]) + 1
            if abs(depth[root.left] - depth[root.right]) <= 1:
                return True
            else:
                flag = False
                return flag
        return dfs(root)

# Other's, Recursive DFS
class Solution(object):
    def isBalanced(self, root):

        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1

# Other's, Iterative Postorder Traversal
class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True
