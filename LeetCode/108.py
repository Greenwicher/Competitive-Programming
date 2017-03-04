__author__ = 'liuweizhi'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1, Recursion
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def bst(root, nums):
            if not nums: return None
            if len(nums) == 1:
                root.val = nums[0]
                return root
            pivot = len(nums) // 2
            root.val = nums[pivot]
            root.left = bst(TreeNode(-1), nums[:pivot])
            root.right = bst(TreeNode(-1), nums[pivot+1:])
            return root
        return bst(TreeNode(-1), nums)