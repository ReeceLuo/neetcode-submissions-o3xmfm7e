import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # directed graph
        # dijkstra's shortest path to each node

        adj_list = [[] for _ in range(n + 1)]
        for u, v, t in times:
            adj_list[u].append((v, t))
        
        # dijkstras - take min edge of all edges we can reach
        heap = []
        heap.append((0, k))
        minTime = 0
        visited = set()
        while heap and len(visited) < n:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            minTime = time
            visited.add(node)
            for neighbor, t in adj_list[node]:
                heapq.heappush(heap, (t + minTime, neighbor))
                
        return minTime if len(visited) == n else - 1
        