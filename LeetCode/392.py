#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 17:33:14 2017

@author: liuweizhi
"""

#%% Version 1 - Greedy
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while (i < len(s) and j < len(t)):
            if s[i] == t[j]: i += 1
            j += 1
        if i == len(s):
            return True
        else:
            return False
                
#%% Version 2 - Iterator
def isSubsequence(self, s, t):
    t = iter(t)
    return all(c in t for c in s)
             
        