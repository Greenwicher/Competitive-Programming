__author__ = 'liuweizhi'

def bfs(maze, start):
    """
    :param maze: List[List[int]], the 01 maze matrix
    :param start: (int, int), the coordinate of starting point
    :return: List[List[int]], cache[i][j] represents the shortest distance from the starting point
    """
    m, n = len(maze), len(maze[0])
    visited = [[False] * n for _ in range(m)]
    cache = [[1e100] * n for _ in range(m)]
    queue = [(start[0], start[1], 1)] # starting point with distance one
    while queue:
        x, y, s = queue.pop(0)
        if not(visited[x][y]):
            cache[x][y] = s
            visited[x][y] = True
            # append all passable unvisited adjacent point into the queue
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= x+i < m and 0 <= y+j < n and maze[x+i][y+j] == 0:
                    queue.append((x+i, y+j, s+1))
    return cache

def answer(maze):
    # your code here
    m, n = len(maze), len(maze[0])
    start_cache = bfs(maze, (0, 0)) # shortest distance from the starting point
    end_cache = bfs(maze, (m-1, n-1)) # shortest distance from the ending point
    ans = start_cache[m-1][n-1] # shortest distance if not remove any walls
    # enumerate all possible walls to be removed
    for x in range(m):
        for y in range(n):
            if maze[x][y] == 1:
                # construct passable adjacent point
                neighbors = [(x+i, y+j) for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                             if 0 <= x+i < m and 0 <= y+j < n and maze[x+i][y+j] == 0]
                # enumerate all the possible new path
                for n1 in neighbors:
                    for n2 in neighbors:
                        if n1 != n2:
                            n1x, n1y = n1
                            n2x, n2y = n2
                            ans = min([ans, start_cache[n1x][n1y]+1+end_cache[n2x][n2y],
                                       end_cache[n1x][n1y]+1+start_cache[n2x][n2y]])
    return ans

print(answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]), 7)
print(answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]), 11)
print(answer([[0,1,1,0,0,0,0],[0,1,1,0,1,1,0],[0,0,0,0,1,1,0],[1,1,1,1,1,1,0]]), 14)
import numpy as np
maze = np.random.randint(0, 2, size=(3,3))
print(maze)
print(answer(maze))