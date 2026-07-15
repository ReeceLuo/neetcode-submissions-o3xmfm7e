class DSU:
    def __init__(self, numNodes):
        self.parents = list(range(numNodes)) # each node starts as own parent
        self.rank = [0] * numNodes
        self.groups = numNodes
    
    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: # same set leader, connecting does not change anything
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parents[py] = px
        self.groups -= 1
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # connected components - use DSU to track groups
        # union nodes with each edge 

        dsu = DSU(n)
        for a, b in edges:
            dsu.union(a, b)
        
        return dsu.groups

