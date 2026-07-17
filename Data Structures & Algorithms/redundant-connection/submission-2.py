class DSU:
    def __init__(self, numNodes):
        self.parents = list(range(numNodes))
        self.rank = [0] * numNodes
        self.groups = numNodes

    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: # same parent
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parents[py] = px
        self.groups -= 1
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # given an undirected graph with no cycles, determine if adding
        # an edge creates a cycle
        # use disjoint set union w/ path compression and smart rank

        # return first edge that causes a cycle
        # num edges is not number of nodes
        maxNode = edges[0][0]
        for a, b in edges:
            maxNode = max(maxNode, a, b)

        dsu = DSU(maxNode + 1)
        for a, b in edges:
            if not dsu.union(a, b):
                return [a, b]
        return edges[-1]




