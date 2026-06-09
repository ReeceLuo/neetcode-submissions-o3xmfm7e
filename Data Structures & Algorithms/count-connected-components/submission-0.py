class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.groups = n
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node]) # path compression, point to root
        return self.parent[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[py] > self.rank[px]: # ensure we always append shorter tree
            px, py = py, px
        self.parent[py] = px
        self.groups -= 1
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for a, b in edges:
            dsu.union(a, b)
        
        return dsu.groups

