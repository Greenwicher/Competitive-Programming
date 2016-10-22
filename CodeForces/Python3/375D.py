# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 20:04:55 2016

@author: liuweizhi
"""

#%% Version 1
# depth first search 
def dfs(i,j):
    # explored already
    if flag[i][j] != -1:
        return 0
    # boundary of land
    elif grid[i][j] == '*':
        flag[i][j] = 0
        return 0
    # water regions
    else:
        flag[i][j] = len(lake)+1    
        # connect with ocean
        if i==0 or i==n-1 or j==0 or j==m-1:
            return -1e99
        else:
            return dfs(i-1,j)+dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1)+1
n,m,k = list(map(int, input().split()))
grid = []
flag = [[-1 for j in range(m)] for i in range(n)]
for _ in range(n):
    grid.append(input())
lake = []
for i in range(1,n-1):
    for j in range(1,m-1):
        # unexplored water regions, i.e. promising new lakes
        if flag[i][j] == -1 and grid[i][j] == '.':
            lake.append((len(lake)+1,dfs(i,j)))
lake = [foo for foo in sorted(lake, key = lambda x:x[1]) if foo[1]>0]
small_lake = [lake[i][0] for i in range(len(lake)-k)]
print([0,sum([lake[i][1] for i in range(len(lake)-k)])][len(lake)>k])
for i in range(n):
    line = []
    for j in range(m):
        line.append([grid[i][j],'*'][flag[i][j] in small_lake])
    print(''.join(line))