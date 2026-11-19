import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # use dijkstra's to find shortest path.
        # shortest path to final node is min time to get to all nodes        

        adj_list = [[] for _ in range(n + 1)]

        for src, target, time in times:
            adj_list[src].append((target, time))
        
        visited = set()

        heap = [(0, k)]
        minTime = 0
        
        while heap and len(visited) < n:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            minTime = time

            for neighbor, timeToNeighbor in adj_list[node]:
                heapq.heappush(heap, (time + timeToNeighbor, neighbor))
        
        return minTime if len(visited) == n else -1


