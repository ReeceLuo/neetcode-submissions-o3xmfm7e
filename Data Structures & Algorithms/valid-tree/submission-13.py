class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
        self.groups = n

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, x, y):
        x_parent, y_parent = self.find(x), self.find(y)
        if x_parent == y_parent:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parents[y_parent] = x_parent
        self.groups -= 1
        if self.rank[x_parent] == self.rank[y_parent]:
            self.rank[x_parent] += 1
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # DSU - Disjoint Set Union
        # Data structure that tracks which elements are associated by
        # representing them with a set leader
            # While building DSU, find the set leaders of two nodes of an edge:
            # if same leader, there is a cycle because there is already a path between them - adding an edge would create a cycle
            # if different, current edge will now add them together
        
        # rank - upper bound on groups height
            # append tree of lower rank to greater
            # use path compression -        
        dsu = DSU(n)
        for x, y in edges:
            if not dsu.union(x, y):
                return False
        
        return dsu.groups == 1






