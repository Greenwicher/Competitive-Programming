#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 00:19:00 2016

@author: liuweizhi
"""

#%%
def dfs(i,j):
    if i == -1 or i == m or j == -1 or j == n:
        return 1
    if visited[i][j]:
        return 1
    elif board[i][j] == 'X':
        visited[i][j] = 1
        return dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)
    return 1
board = ["X..X.X","...X.X","...X.X"]
ans = 0
m, n = len(board), len(board[0])
visited = [[0]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        if not(visited[i][j]) and board[i][j] == 'X':
            dfs(i,j)
            ans += 1
print(ans)