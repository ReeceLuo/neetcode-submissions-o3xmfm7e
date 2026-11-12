class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n
        self.groups = n

    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: # same set leader, same group, cyclic
            return False
        if self.ranks[px] < self.ranks[py]:
            px, py = py, px
        self.parents[py] = px
        self.groups -= 1
        if self.ranks[px] == self.ranks[py]:
            self.ranks[px] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree - connected, acyclic, undirected graph
        # use DSU to check for cycles and track groups
            # if no cycles and one group, true

        dsu = DSU(n)
        for x, y in edges:
            if not dsu.union(x, y):
                return False
            
        return dsu.groups == 1







