# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 18:22:17 2016

@author: liuweizhi
"""

#%% Version 1
# add new sock to same_color_sock group and update frequency of color
def update_group(gid, id):
    id -= 1
    if not(c[id] in group[gid]):
        group[gid][c[id]] = 1
    else:
        group[gid][c[id]] += 1
    return
    
I = lambda: list(map(int, input().split()))
n, m, k = I()
c = I()
group_id = {} #group id of each sock
group = [] #same_color_sock group and frequency of color
for i in range(m):
    l, r = I()
    #check whether sock l, r are in existing same_color_sock group
    #the following code is wrong (possible two groups can be combined)
    if not(l in group_id) and not(r in group_id):
        id = len(group)        
        group_id[l], group_id[r] = [id] * 2
        group.append({})
        update_group(group_id[l], l)
        update_group(group_id[r], r)
    elif (l in group_id) and not(r in group_id):
        group_id[r] = group_id[l]
        update_group(group_id[r], r)
    elif not(l in group_id) and (r in group_id):
        group_id[l] = group_id[r]
        update_group(group_id[l], l)
ans = 0
#different same_color_sock groups
for foo in group:
    max_color_num = -1
    num = 0
    for k in foo:
        num += foo[k]
        if foo[k]>max_color_num: 
            max_color_num = foo[k]
    ans += num - max_color_num
print(ans)

#%% Version 2
from collections import defaultdict
def dfs(i):
    if visited[i]:
        return
    else:
        visited[i] = True
        #update the color frequency in the same_color_sock group
        group[-1][c[i-1]] = group[-1].get(c[i-1],0) + 1
        #process the adjacent socks
        for j in adjacent[i]:
            dfs(j)
    return 
I = lambda: list(map(int, input().split()))
n, m, k = I()
c = I()
adjacent = defaultdict(lambda: set())
visited = defaultdict(lambda: False)
group = []
for i in range(m):
    l,r = I()
    #record the adjacent socks
    adjacent[l].add(r)
    adjacent[r].add(l)
for i in range(1, n+1):
    if visited[i]:
        continue
    else:
        #new same_color_sock group and run dfs
        group.append({})
        dfs(i)
ans = 0        
for g in group:
    max_color_num = -1
    num = 0
    for color in g:
        num += g[color]
        if g[color]>max_color_num: 
            max_color_num = g[color]
    ans += num - max_color_num
print(ans)    
    
