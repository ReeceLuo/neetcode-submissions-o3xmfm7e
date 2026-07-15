
class DSU:
    def __init__(self, numNodes):
        self.parents = list(range(numNodes)) #initialize as all parents are itself
        self.rank = [0] * numNodes
        self.groups = numNodes
    
    def find(self, node): # O(1) amortized time
        # path compression
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parents[py] = px # union
        self.groups -= 1
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree - acyclic, undirected graph
        # check for cycles in undirected graph - DSU
        dsu = DSU(n)
        for a, b in edges:
            if not dsu.union(a, b):
                return False
        
        return dsu.groups == 1
