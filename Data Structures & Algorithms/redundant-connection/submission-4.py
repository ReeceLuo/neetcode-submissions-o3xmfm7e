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
       # initially contains no cycles, now an additional edge causes cycle
       # for undirected graph cycle detection, use disjoint set union

       # go through every edge while building dsu. track last one that causes cycle 

        dsu = DSU(len(edges))
        res = None
        for x, y in edges:
            if not dsu.union(x - 1, y - 1):
                res = [x, y]
        
        return res


