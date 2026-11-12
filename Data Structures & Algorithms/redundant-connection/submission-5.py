class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n
    
    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.ranks[px] < self.ranks[py]:
            px, py = py, px
        self.parents[py] = px
        if self.ranks[px] == self.ranks[py]:
            self.ranks[px] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # nodes listed from 1 to n
        # undirected graph, if no cycles and n - 1 edges, it is tree
        # added an edge that caused a cycle.
        # if mulitple, return the last

        # use DSU to track when cycles are made

        # there are n - 1 edges initially, aded one edge, so n edges
        # initialize DSU w/ len(edges)
        dsu = DSU(len(edges))

        redundant = None

        for a, b in edges:
            if not dsu.union(a - 1, b - 1):
                redundant = [a, b]

        return redundant







