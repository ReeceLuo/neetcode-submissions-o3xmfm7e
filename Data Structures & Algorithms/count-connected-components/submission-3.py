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
        if px == py:
            return False
        if self.ranks[px] < self.ranks[py]:
            px, py = py, px
        self.parents[py] = px
        self.groups -= 1
        if self.ranks[px] == self.ranks[py]:
            self.ranks[px] += 1
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # use dsu to keep track of groups
        # if two nodes have same leader, in same connected group
        # if not, join them and reduce groups

        dsu = DSU(n)
        for x, y in edges:
            dsu.union(x, y)
        return dsu.groups