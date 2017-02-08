#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 15:55:28 2017

@author: liuweizhi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#%% Version 1 - Decomposition
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Treeroot
        :type k: int
        :rtype: int
        """
        def rank(root):
            if root:
                if root.left or root.right:
                    return rank(root.left) + rank(root.right) + 1
                else:
                    return 1
            else:
                return 0  
        _k = rank(root.left) + 1
        if _k < k:
            return self.kthSmallest(root.right, k - _k)
        elif _k > k:
            return self.kthSmallest(root.left, k)
        else:
            return root.val
            
            
#%% Version 2 - Binary Search
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Treeroot
        :type k: int
        :rtype: int
        """