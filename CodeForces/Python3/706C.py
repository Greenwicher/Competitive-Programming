#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 13:47:02 2017

@author: liuweizhi
"""
# Problem Description: http://codeforces.com/problemset/problem/706/C

# read the input
I = lambda: list(map(int, input().split()))
n = I()[0]
c = I()
word = []
for _ in range(n):
    w = input()
    word.append(w)
    
# initialize the cost dp array 
# dp[i][0] represents the smallest cost if word[i] is not reversed
# dp[i][1] represents the smallest cost if word[i] is reversed
dp = [[1e100]*2 for _ in range(n)]
dp[0][0] = 0
dp[0][1] = c[0]

# calculate the dp array 
for i in range(n-1):
    # not reverse word[i+1]
    if word[i+1] >= word[i]:
        dp[i+1][0] = min(dp[i+1][0], dp[i][0])
    if word[i+1] >= word[i][::-1]:
        dp[i+1][0] = min(dp[i+1][0], dp[i][1])
    # reverse word[i+1]
    if word[i+1][::-1] >= word[i]:
        dp[i+1][1] = min(dp[i+1][1], c[i+1] + dp[i][0])
    if word[i+1][::-1] >= word[i][::-1]:
        dp[i+1][1] = min(dp[i+1][1], c[i+1] + dp[i][1])

# print the output
if min(dp[-1]) < 1e100:
    print(min(dp[-1]))
else:
    print(-1)
        
    