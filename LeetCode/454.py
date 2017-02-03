#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 19:07:49 2017

@author: liuweizhi
"""

#%% Version 1 - Wrong Answer
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        A, B, C, D = list(map(sorted, [A, B, C, D]))
        self.init(A, B, C, D)
        r = self.binary_search_upper()
        l = self.binary_search_lower()
        return r - l - 1
        
    def binary_search_upper(self):
        # find the index (reshaped into one dimension) of the first element > 0
        l, r = [0] * 4, [self.n-1] * 4
        decode, code, value = self.decode, self.code, self.value
        while(code(l) < code(r)):
            m = decode((code(l) + code(r) // 2))
            if value(m) <= 0:
                l = decode(code(m) + 1)
            else:
                if (code(m) > 0) and value(decode(code(m) - 1)) > 0:
                    r = decode(code(m) - 1)
                else:
                    return code(m)
        if value(l) > 0:
            return code(l)
        elif value(r) > 0:
            return code(r)
        else:
            return -1
            
    def binary_search_lower(self):
        # find the index (reshaped into one dimension) of the last element < 0
        l, r = [0] * 4, [self.n-1] * 4
        decode, code, value = self.decode, self.code, self.value
        while(code(l) < code(r)):
            m = decode((code(l) + code(r) // 2))
            if value(m) >= 0:
                r = decode(code(m) - 1)
            else:
                if (code(m) < self.n - 1) and value(decode(code(m) + 1)) < 0:
                    r = decode(code(m) + 1)
                else:
                    return code(m)
        if value(l) < 0:
            return code(l)
        elif value(r) < 0:
            return code(r)
        else:
            return -1
            
            
    def value(self, index):
        print(index)
        ans = 0
        for L, i in zip([self.A, self.B, self.C, self.D], index):
            ans += L[i]
        return ans
        
    def code(self, index):
        ans = sum([index[i] * (self.n ** i) for i in range(4)])
        return ans
    
    def decode(self, num):
        index, i = [0] * 4 , 0
        while(num):
            index[i] = num % self.n
            num //=  self.n
            i += 1
        return index
        
    def init(self, A, B, C, D):
        self.n = len(A)
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        return  
        
A, B, C, D = [1,2], [-2,-1], [-1,2], [0,2]
test = Solution()
test.fourSumCount(A, B, C, D)

#%% Version 2 
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = {}
        for a in A:
            for b in B:
                AB[a+b] = AB.get(a+b, 0) + 1
        ans = 0
        for c in C:
            for d in D:
                if -c-d in AB: ans += AB[-c-d]
        return ans


