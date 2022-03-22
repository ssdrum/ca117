#!/usr/bin/env python3

# https://www.cs.yale.edu/homes/aspnes/pinewiki/DepthFirstSearch.html for info

class Graph(object):

    def __init__(self, V):
        self.V = V  # number of vertices in graph
        self.adj = {}  # number of edges (which vertices are connected to which)
        for v in range(V):
            self.adj[v] = []  # generates dictionary with keys: 0 to V-1, each with a list of connected vertices

    # adds vertice v to the graph. connects it to another verticey w
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)


class DFSPaths(object):
    # g = graph object, s = starting vertice
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.visited = [False for _ in range(g.V)]  # necessary to avoid visiting same node twice. Index = vertice
        self.parent = [False for _ in range(g.V)]
        self.dfs(s)

    # strategy: choose initial vertice (v)
    def dfs(self, v):
        self.visited[v] = True  # set currently visited node to true
        for w in self.g.adj[v]:  # for each successor of v
            if not self.visited[w]:  # if successor hasn't been visited
                self.parent[w] = v  # add v as a parent of successor
                self.dfs(w)  # call function recursively with successor

    # Return True if there is a path from s to v
    def hasPathTo(self, v):
        return self.visited[v]

    # Return path from s to v (or None should one not exist)
    def pathTo(self, v):
        if self.hasPathTo(v):  # if there is a path from s to v
            vcpy = v
            path = []
            while vcpy != self.s:
                path.append(self.parent[vcpy])
                vcpy = self.parent[vcpy]
            path.reverse()
            return path + [v]


def main():
    pass


if __name__ == "__main__":
    main()