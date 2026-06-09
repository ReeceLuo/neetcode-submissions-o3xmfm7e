class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.groups = n
    
    # path compression - recursively look for parent node until
    # the parent is the node iself (root) and point the node to this root
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node]) 
        return self.parent[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:    # have same set leader -> same group
            return False
        if self.rank[py] > self.rank[px]:
            px, py = py, px
        # appends one root to the other
        self.parent[py] = px    # union
        self.groups -= 1
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)

        for a, b in edges:
            if not dsu.union(a, b):
                return False
        return dsu.groups == 1




