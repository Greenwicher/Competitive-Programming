def answer(entrances, exits, path):
    """
    find the maximum flow given multiple sources and multiple sinks
    :param entrances: List[int], indicate the index of sources
    :param exits: List[int], indicate the index of sinks
    :param path: List[List[int]], path[A][B] = C means the capacity from A to B is C
    :return: the maximum flow
    """
    def dfs(s, t, f, dist):
        """
        find and augment a blocking flow, and finally return the minimum of residual capacity
        :param s: int, the index of source
        :param t: int, the index of sink
        :param f: int, the minimum of residual capacity so far
        :param dist: List[int], dist[i] is the shortest distance from s to i
        :return: the minimum of residual capacity
        """
        if s == t:
            return f
        for u, connected in enumerate(G[s]):
            if connected and u != s:
                if F[s][u] < C[s][u] and dist[u] == dist[s] + 1:
                    delta_flow = dfs(u, t, min(f, C[s][u]-F[s][u]), dist)
                    if delta_flow > 0:
                        F[s][u] += delta_flow
                        F[u][s] -= delta_flow
                        return delta_flow
        return 0

    def bfs(s, t):
        """
        construct the level graph dist[], and check whether the sink t is in the level graph
        :param s: int, the index of source
        :param t: int, the index of sink
        :return: the level graph dist (List[int]) and whether t is in the level graph (Bool)
        """
        dist = [None] * len(G)
        queue = [s]
        dist[s] = 0
        while queue:
            v = queue.pop(0)
            for u, connected in enumerate(G[v]):
                if connected and u != v:
                    if F[v][u] < C[v][u] and dist[u] is None:
                        dist[u] = dist[v] + 1
                        queue.append(u)
        return dist[t] is not None, dist

    def max_flow(s, t):
        """
        find the maximum flow given adjacent matrix of graph G, capacity matrix C, the source s and the source t
        :param s: int, the index of source
        :param t: int, the index of sink
        :return: maximum_flow, int
        """
        maximum_flow = 0
        while True:
            # construct the level graph
            [reachable, dist] = bfs(s, t)
            # exit if no augmenting paths from s to t are found
            if not reachable:
                break
            # augment the blocking flow repeatedly by DFS based on level graph
            while True:
                delta_flow = dfs(s, t, 1e100, dist)
                maximum_flow += delta_flow
                if delta_flow == 0:
                    break
        return maximum_flow

    def add_edge(i, j, capacity):
        """
        construct the adjacent matrix of graph G, and the capacity matrix C
        :param i: int, index of tail vertex
        :param j: int, index of head vertex
        :param capacity: the capacity of edge from i to j
        :return: None
        """
        G[i][j], G[j][i] = 1, 1
        C[i][j] = capacity
        return

    # construct the adjacency matrix of graph G, capacity matrix C, and initialize the flow matrix F
    n = len(path)
    G, C, F = [[[0] * (n+2) for _ in range(n+2)] for _ in range(3)]
    # add Phantom single source and single sink
    for source in entrances:
        add_edge(0, source+1, 1e100)
    for sink in exits:
        add_edge(sink+1, n+1, 1e100)
    for i in range(n):
        for j in range(n):
            if i != j and path[i][j]:
                add_edge(i+1, j+1, path[i][j])
    # solve the maximum flow problem by Dinic's algorithm
    ans = max_flow(0, n+1)
    return ans

print(answer([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]), 6)
print(answer([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]), 16)
print(answer([0], [5], [[1,2,3,4,5],[5,4,3,2,1],[1,2,3,4,5],[5,4,3,2,1],[1,2,3,4,5]]))
print(answer([0], [2], [[1,2,3],[3,0,1],[0,0,0]]))
print(answer([0], [2], [[1,2,3],[3,2,1],[1,2,3]]))
