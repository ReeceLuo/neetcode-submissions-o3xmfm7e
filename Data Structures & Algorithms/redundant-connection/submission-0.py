class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: # same set leader so same group
            return False
        if self.rank[py] > self.rank[px]:
            px, py = py, px
        self.parents[py] = px # append py (root) to px (root)
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # given an adjacnecny list
        # use disjoint set union - return latest edge that creates cycle

        dsu = DSU(len(edges))
        res = []
        for a, b in edges:
            if not dsu.union(a - 1, b - 1):
                res = [a, b]
        return res
