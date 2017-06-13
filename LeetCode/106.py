# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Version 1, Recursive Construction, O(n^2) time complexity, O(n) space complexity
import sys
sys.setrecursionlimit(10000)
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def recursive(root, _inorder, _postorder):
            if len(_inorder) == 1:
                return
            i = _inorder.index(root.val)
            left_inorder, right_inorder = _inorder[:i], _inorder[i+1:] # left and right tree of inorder sequence
            j = len(left_inorder)
            left_postorder, right_postorder = _postorder[:j], _postorder[j:-1] # left and right tree of preorder sequence
            if left_postorder:
                root.left = TreeNode(left_postorder[-1])
                recursive(root.left, left_inorder, left_postorder)
            if right_postorder:
                root.right = TreeNode(right_postorder[-1])
                recursive(root.right, right_inorder, right_postorder)
            return
        if not postorder:
            return []
        else:
            ans = TreeNode(postorder[-1])
            recursive(ans, inorder, postorder)
            return ans

s = Solution()
print(s.buildTree([4,2,5,1,None,3,6], [4,5,2,None,6,3,1]))