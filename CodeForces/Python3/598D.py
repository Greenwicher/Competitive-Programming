# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:02:56 2016

@author: liuweizhi
"""

#%% Version 1: given (x,y) search valide empty regions and calculate max_pic_num
#Search irreducible valid regions recurisvely
#!!no need to return any value for this recurisve function
def searchPicLayout(m,x,y):
    global pic
    global visit
    #visit (x,y)
    visit.add((x,y))
    #valid direction
    move = [(0,-1),(1,0),(0,1),(-1,0)]
    for i in range(len(move)):
        #find neighbot (ith direction)                   
        d = move[i]
        nx,ny = x+d[0],y+d[1]
        #check neighbor        
        if m[nx][ny] != '*':
            #check key of (nx,ny) in explore
            if not((nx,ny) in visit):                
                #explore new valid unvisited point
                searchPicLayout(m,nx,ny)
        else:
            #impassable point and mark the picture
            pic[nx][ny] += 1
#Read Input
I = lambda:map(int,input().split())
n,m,k = I()
museum = []
for _ in range(n):
    museum.append(input())
#Output
for _ in range(k):
    x,y = I()
    #records layout of pictures, 1 represents picture exists
    pic = [[0 for j in range(m)] for i in range(n)]
    #records visited points
    visit = set()
    #find the pictures can be viewed
    searchPicLayout(museum,x-1,y-1)
    #Output best solutions
    print(sum([sum(r) for r in pic]))
    
#%% Version 2: based on Version 1, but make indexing for all empty points before retrieving informaiton
#Search irreducible valid regions recurisvely for (x,y)
#!!no need to return any value for this recurisve function
def searchPicLayout(m,x,y):
    global pic
    global visit
    #visit (x,y)
    visit.add((x,y))
    #valid direction
    move = [(0,-1),(1,0),(0,1),(-1,0)]
    for i in range(len(move)):
        #find neighbot (ith direction)                   
        d = move[i]
        nx,ny = x+d[0],y+d[1]
        #check neighbor        
        if m[nx][ny] != '*':
            #check key of (nx,ny) in explore
            if not((nx,ny) in visit):                
                #explore new valid unvisited point
                searchPicLayout(m,nx,ny)
        else:
            #impassable point and mark the picture
            pic[nx][ny] += 1
#Read Input
I = lambda:map(int,input().split())
n,m,k = I()
museum = []
for _ in range(n):
    museum.append(input())
#Indexing
ans = [[0 for j in range(m)] for i in range(n)]
for x in range(1,n-1):
    for y in range(1,m-1):
        #search itteducible valid regions for empty unvisited point (i,j)
        if museum[x][y]=='.' and ans[x][y]==0:
            #records layout of pictures, 1 represents picture exists
            pic = [[0 for j in range(m)] for i in range(n)]
            #records visited points
            visit = set()
            #searching valid regions
            searchPicLayout(museum,x,y)
            max_pic_num = sum([sum(r) for r in pic])
            for p in visit:
                ans[p[0]][p[1]] = max_pic_num            
#Output
for _ in range(k):
    x,y = I()
    print(ans[x-1][y-1])
    
#%% Version 3: try to write it recurrencely instead of recurisively
def dfs(mat,i):
    global visit
    visit.add(i)
    for j in range(len(mat)):
        if mat[i][j]==1 and not(j in visit):
            dfs(mat,j)
#Read Input
I = lambda:map(int,input().split())
n,m,k = I()
museum = []
for _ in range(n):
    museum.append(input())
#Indexing
ans = [] # max_pic_num for each region
region = [[-1 for j in range(m)] for i in range(n)] # region id for each point
region_id = -1
size = n*m
region_join = [[0 for j in range(size)] for i in range(size)] # determine wheter region i and region j connects
for i in range(size):
    region_join[i][i] = 1
for x in range(1,n-1):
    for y in range(1,m-1):
        if museum[x][y] == '.':
            r1,r2 = region[x-1][y],region[x][y-1]
            #same region with (x-1,y)
            if museum[x-1][y]=='.' and museum[x][y-1]!='.':
                region[x][y] = r1
            #same region with (x,y-1)
            elif museum[x-1][y]!='.' and museum[x][y-1]=='.':
                region[x][y] = r2
            #perhaps link between two regions
            elif museum[x-1][y]=='.' and museum[x][y-1]=='.':
                region[x][y] = r1 #arbitrary region id
                # r1/r2 connects r2/r1
                region_join[r1][r2] = 1
                region_join[r2][r1] = 1
            else:
                #new region
                region_id += 1
                ans.append(0)
                region[x][y] = region_id
            #update max_pic_num for this region
            ans[region[x][y]] += [museum[x][y-1],museum[x+1][y],museum[x][y+1],museum[x-1][y]].count('*')
#Output
for _ in range(k):
    x,y = I()
    visit = set()
    dfs(region_join,region[x-1][y-1])
    print(sum([ans[i] for i in visit]))

#%% Version 4: based on Version 1, but make indexing for already retrieved information
#Search irreducible valid regions recurisvely for (x,y)
#!!no need to return any value for this recurisve function
def searchRegion(m,x,y):
    global visit
    #visit (x,y)
    visit.add((x,y))
    #valid direction
    move = [(0,-1),(1,0),(0,1),(-1,0)]
    for i in range(len(move)):
        #find neighbot (ith direction)                   
        d = move[i]
        nx,ny = x+d[0],y+d[1]
        #check neighbor        
        if m[nx][ny] == '.' and not((nx,ny) in visit):
            searchRegion(m,nx,ny)

#Read Input
I = lambda:map(int,input().split())
n,m,k = I()
museum = []
for _ in range(n):
    museum.append(input())
#Indexing
ans = [] #max_pic_num for each region
region = [[-1 for j in range(m)] for i in range(n)] # region id for each point
region_id = -1
for _ in range(k):
    x,y = I()
    #check wheter region including (x,y) is explored    
    if region[x-1][y-1] == -1:
        #new region
        region_id += 1
        #records visited points
        visit = set()
        #searching valid regions
        searchRegion(museum,x-1,y-1)
        #update region id and calculate max_pic_num
        max_pic_num = 0
        for p in visit:
            a,b = p[0],p[1] #cannot use x,y as var_name
            region[a][b] = region_id
            max_pic_num += [museum[a][b-1],museum[a+1][b],museum[a][b+1],museum[a-1][b]].count('*')
        #update ans
        ans.append(max_pic_num)
    print(ans[region[x-1][y-1]])

#%% Version 5: forked by SomeRandomGuy, 14440455	
#retrieve region i which includes cell (x,y) and 
#return the max_pic_num and mark the region id for each cell
def search(x,y,i):
    global region
    #impassable cell
    if museum[x][y] == '*': return 1
    #already visited
    if region[x][y] != -1: return 0
    #mark region id
    region[x][y] = i
    #explore recursively (dfs)
    return search(x,y-1,i)+search(x+1,y,i)+search(x,y+1,i)+search(x-1,y,i)   
#Input
I = lambda:map(int,input().split())
n,m,k = I()
museum = []
for _ in range(n):
    museum.append(input())
#Processing
ans = [0 for i in range(n*m)] #max_pic_num for some input cell
region = [[-1 for j in range(m)] for i in range(n)] #region id for each point
for i in range(k):
    x,y = I()
    #unexplored
    if region[x-1][y-1] == -1:
        ans[i] = search(x-1,y-1,i)
    #Output
    print(ans[region[x-1][y-1]])