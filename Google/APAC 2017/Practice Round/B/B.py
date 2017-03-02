#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 22:52:28 2017

@author: liuweizhi
"""

#%% Small Case 
def solve_small(N, K, position):
    ans = 0
    for a in position[0]:
        for b in position[1]:
            for c in position[2]:
                for d in position[3]:
                    ans += (a^b^c^d == K)
    return ans
    
#%% Large Case
def solve_large(N, K, position):
    ans = 0
    from collections import defaultdict
    xor1 = defaultdict(int)
    for a in position[0]:
        for b in position[1]:
            xor1[a^b] += 1
    xor2 = [c^d for c in position[2] for d in position[3]]
    xor3 = [cd^K for cd in xor2]
    ans = sum([xor1[foo] for foo in xor3])
    return ans

#%% Solve
f_in = open('B-large-practice.in', 'r')
f_out = open('B-large-practice.out', 'w')

I = lambda x: list(map(int, x.strip().split()))
T = int(f_in.readline())
for i in range(T):
    N, K = I(f_in.readline())
    position = []
    for _ in range(4):
        position.append(I(f_in.readline()))
    ans = solve_large(N,K,position)
    f_out.write('Case #%d: %d\n' % (i+1, ans))
f_in.close()
f_out.close()
