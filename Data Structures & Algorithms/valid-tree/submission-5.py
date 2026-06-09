from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no duplicate
        # valid tree - no cycles, one graph total
        # union-find: find set leader, combine sets
        # if an edge has two vertices with same set leader,
        # they are of the same set. so the edge would make the tree
        # invlaid

        # use some graph traversal to check for cycles

        adj_list = [[] for i in range(n)]
        visited = set()

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        q = deque()
        q.append(0)
        visited.add(0)

        while q:
            node = q.popleft()
            for neighbor in adj_list[node]:
                if neighbor in visited:
                    return False
                adj_list[neighbor].remove(node)
                q.append(neighbor)
                visited.add(neighbor)
        
        return len(visited) == n


